from __future__ import with_statement
import os
from fabric.api import *
from fabric.colors import red, green
from fabric.contrib.files import exists
from fabric.context_managers import shell_env
from contextlib import contextmanager as _contextmanager


env.project_name = 'aashe-rc'
env.repos = 'ssh://hg@bitbucket.org/aashe/aashe-rc'
env.uwsgi_service_name = 'uwsgi'
env.current_symlink_name = 'current'
env.previous_symlink_name = 'previous'
env.virtualenv_name = 'env'
env.remote_vars = {}

@_contextmanager
def virtualenv():
    '''
    Custom fabric contextmanager that lets you run fabric
    commands (via sudo(), run(), etc.) with a virtualenv
    activated. Uses the `activate` fabric env attribute
    as the virtualenv activation command.

    Usage:
        with(virtualenv()):
            run("python manage.py syncdb")
    '''
    with cd(env.remote_path):
        with shell_env(**env.remote_vars):
            with prefix(env.activate):
                yield

def dev():
    '''
    Configure the fabric environment for the dev server(s).
    '''
    env.user = 'releaser'
    env.hosts = ['www.aashedev.org']
    env.remote_path = '/var/www/django_projects/aashe-rc'
    env.django_settings = 'rc.settings.development'
    env.activate = 'source %s/env/bin/activate' % env.remote_path
    env.uwsgi_service_name = 'aashe-rc'
    if os.environ.has_key('FABRIC_DEV_PASSWORD'):
        env.password = os.environ['FABRIC_DEV_PASSWORD']
    env.requirements_txt = 'requirements/dev.txt'
    env.release_path = '%s/current' % env.remote_path    
    
def new():
    '''
    Configure the fabric environment for the dev server(s).
    '''
    env.user = 'releaser'
    env.hosts = ['new.aashe.org']
    env.remote_path = '/var/www/django_projects/aashe-rc'
    env.django_settings = 'rc.settings.new_settings'
    env.activate = 'source %s/env/bin/activate' % env.remote_path
    env.uwsgi_service_name = 'aashe-rc'
    env.release_path = '%s/current' % env.remote_path
    
def production():
    '''
    Configure the fabric environment for the production server(s).
    '''
    env.user = 'releaser'
    env.hosts = ['www.aashe.org']
    env.remote_path = '/var/www/django_projects/aashe-rc'
    env.django_settings = 'rc.settings.production'
    env.activate = 'source %s/env/bin/activate' % env.remote_path
    env.uwsgi_service_name = 'aashe-rc'
    if os.environ.has_key('FABRIC_PRODUCTION_PASSWORD'):
        env.password = os.environ['FABRIC_PRODUCTION_PASSWORD']
    env.requirements_txt = 'requirements/prod.txt'
    # set a sane default for release_path so that Fabric tasks like
    # syncdb, reset, etc. still work outside of deployment scenario
    env.release_path = '%s/current' % env.remote_path

def deploy():
    '''
    Generic deploy function to deploy a release to the configured
    server. Servers are configured via other functions (like dev).

    For example, to deploy to the dev server, use the fabric command:

    $ fab dev deploy
    '''
    env.branch_name = prompt("Revision, branch or tag name (blank for default): ")
    if not env.branch_name:
        env.branch_name = 'default'
    env.changeset_id = local('hg id -r %s -i' % env.branch_name, capture=True)
    export()
    requirements()
    if not test():
        print(red("[ ERROR: Deployment failed to pass test() on remote. Exiting. ]"))
    else:
        print(green("[ PASS: Deployment passed test() on remote. Continuing... ]"))
    config()
    restart()

def export():
    '''
    Export the designated revision, branch or tag and then upload
    and extract the tarfile to the server. Create a code archive
    locally instead of a server-side checkout of the repository.
    '''
    export_path = '%s_%s' % (env.branch_name,
                             env.changeset_id)
    tarfile = '%s.tar.gz' % export_path
    local('hg archive -r %(branch)s -t tgz %(tarfile)s' %
          {'branch': env.branch_name, 'tarfile': tarfile})
    put(tarfile, env.remote_path)
    local("rm %s" % tarfile)
    with cd(env.remote_path):
        # extract tarfile to export path
        run('tar xvzf %s' % tarfile)
        run('rm -rf %s' % tarfile)
        env.release_path = '%s/%s' % (env.remote_path, export_path)

def requirements():
    '''
    Refresh or create the remote virtualenv site-packages using
    the project's requirements.txt file.
    '''
    with virtualenv():
        print(green("[ Updating virtualenv via requirements... ]"))
        if not hasattr(env, 'release_path'):
            env.release_path = '%s/current' % env.remote_path
        run('pip install -r %s/%s' % (env.release_path, env.requirements_txt))
        
def test():
    '''
    Test our installation in a few ways.

    TODO: Actually run tests!
    '''
    with virtualenv():
        with cd(env.release_path):
            result = run('python manage.py validate --settings=%s' % env.django_settings)
            print 'test() result was %s' % result
    return result.succeeded        
        
def update_symlinks():
    with cd(env.remote_path):
        if exists(env.previous_symlink_name):
            # get the real directory pointed to by previous
            previous_path = run('readlink %s' % env.previous_symlink_name)
            run('rm %s' % env.previous_symlink_name)
            run('rm -rf %s' % previous_path)            
        if exists(env.current_symlink_name):
            # get the real directory pointed to by current
            current_path = run('readlink %s' % env.current_symlink_name)
            # make current the new previous
            run('ln -s %s %s' % (current_path, env.previous_symlink_name))
            run('rm %s' % env.current_symlink_name)
        # update "current" symbolic link to new code path
        run('ln -s %s %s' % (env.release_path, env.current_symlink_name))
        
def config():
    '''
    Configure the exported and uploaded code archive.
    '''
    with virtualenv():
        with cd(env.release_path):
            # enter new code location, activate virtualenv and collectstatic
            run('python manage.py collectstatic --settings=%s --noinput' %
                env.django_settings)
    update_symlinks()

def loadrc():
    '''
    Clear and load RC data.
    '''
    with virtualenv():
        with cd(env.release_path):
            run('python manage.py reset operations pae education policies programs --noinput --settings=%s' %
                env.django_settings)
            run('python manage.py loadrc --settings=%s' %
                env.django_settings)

def restart():
    '''
    Reboot uwsgi server.
    '''
    sudo("service %s restart" % env.uwsgi_service_name)

def syncdb():
    '''
    Run "manage.py syncdb".
    '''
    with virtualenv():
        with cd(env.release_path):
            run('python manage.py syncdb --noinput --settings=%s' %
                env.django_settings)

def reset(app_name):
    with virtualenv():
        with cd(env.release_path):
            run('python manage.py reset %s --noinput --settings=%s' %
                (app_name, env.django_settings))

def findlinks():
    '''
    Run "manage.py findlinks".
    '''
    with virtualenv():
        with cd("%s/current/rc" % env.remote_path):
            run('python manage.py findlinks --settings=%s' %
                env.django_settings)

def checklinks():
    '''
    Run "manage.py checklinks".
    '''
    with virtualenv():
        with cd("%s/current/rc" % env.remote_path):
            run('python manage.py checklinks --settings=%s' %
                env.django_settings)

def loadcms():
    '''
    Clear and load cms data.
    '''
    with virtualenv():
        with cd("%s/current/rc" % env.remote_path):
            run('python manage.py reset cms treemenus --noinput --settings=%s' %
                env.django_settings)
            run('python manage.py loaddata cms/fixtures/menu_data.json --settings=%s' %
                env.django_settings)
            run('python manage.py loaddata cms/fixtures/menu_item_data.json --settings=%s' %
                env.django_settings)
            run('python manage.py loaddata cms/fixtures/menu_extension_data.json --settings=%s' %
                env.django_settings)
            run('python manage.py loadpages --settings=%s' %
                env.django_settings)

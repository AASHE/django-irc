from __future__ import with_statement
from fabric.api import *
from contextlib import contextmanager as _contextmanager


env.project_name = 'aashe-rc'
env.repos = 'ssh://hg@bitbucket.org/jesselegg/aashe-rc'

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
    with cd(env.path):
        with prefix(env.activate):
            yield

def dev():
    '''
    Configure the fabric environment for the dev server(s).
    '''
    env.user = 'releaser'
    env.hosts = ['rc2-dev.aashe.org']
    env.path = '/var/www/django_projects/aashe-rc'
    env.django_settings = 'rc.dev_settings'
    env.activate = 'source %s/env/bin/activate' % env.path

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
    config()

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
    put(tarfile, env.path)
    with cd(env.path):
        # extract tarfile to export path
        run('tar xvzf %s' % tarfile)
        run('rm -rf %s' % tarfile)
        env.release_path = '%s/%s' % (env.path, export_path)

def requirements():
    '''
    Refresh or create the remote virtualenv site-packages using
    the project's requirements.txt file.
    '''
    with virtualenv():
        print("Updating virtualenv via requirements...")
        sudo('pip install -r %s/current/requirements.txt' % env.path)

def config():
    '''
    Configure the exported and uploaded code archive.
    '''
    with cd(env.path):
        # update "current" symbolic link to new code path
        run('rm current')
        run('ln -s %s current' % env.release_path)
    with virtualenv():
        with cd(env.release_path):
            # enter new code location, activate virtualenv and collectstatic
            run('python rc/manage.py collectstatic --settings=%s --noinput' %
                env.django_settings)
    # change group permissions
    #sudo('chgrp -R admin %s/*' % env.path)

def loadrc():
    '''
    Clear and load RC data.
    '''
    with virtualenv():
        with cd("%s/current/rc" % env.path):
            run('python manage.py reset operations pae education policies programs --noinput --settings=%s' %
                env.django_settings)
            run('python manage.py loadrc --settings=%s' %
                env.django_settings)

def restart():
    '''
    Reboot uwsgi server.
    '''
    sudo("service uwsgi restart")

def syncdb():
    '''
    Run "manage.py syncdb".
    '''
    with virtualenv():
        with cd("%s/current/rc" % env.path):
            run('python manage.py syncdb --noinput --settings=%s' %
                env.django_settings)
                
def loadcms():
    '''
    Clear and load cms data.
    '''
    with virtualenv():
        with cd("%s/current/rc" % env.path):
            run('python manage.py reset cms treemenus --noinput --settings=%s' %
                env.django_settings)
            run('python manage.py loaddata %s/current/rc/cms/fixtures/*.json --settings=%s' %
                    env.django_settings)
            run('python manage.py loadpages --settings=%s' %
                env.django_settings)

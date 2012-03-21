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
    env.changeset = local('hg id -r %s -i' % env.branch_name, capture=True)
    export()
    config()

def export():
    '''
    Export the designated revision, branch or tag and then upload
    and extract the tarfile to the server. Create a code archive
    locally instead of a server-side checkout of the repository.
    '''
    pass

def requirements():
    '''
    Refresh or create the remote virtualenv site-packages using
    the project's requirements.txt file.
    '''
    with virtualenv():
        print(green("Updating virtualenv via requirements..."))
        run('pip install -r %s/current/requirements.txt' % env.path)

def config():
    '''
    Configure the exported and uploaded code archive.
    '''
    pass

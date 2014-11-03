__author__ = 'ksaric'

from fabric.api import *

# the user to use for the remote commands
env.user = 'iii-dev'
# the servers where the commands are executed
env.hosts = ['10.168.2.71', ]


def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)


def deploy():
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '/tmp/galileo.tar.gz')
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    run('mkdir /tmp/galileo')
    with cd('/tmp/galileo'):
        run('tar xzf /tmp/galileo.tar.gz')
        # now setup the package with our virtual environment's
        # python interpreter
        run('/var/www/galileo/env/bin/python setup.py install')
    # now that all is set up, delete the folder again
    run('rm -rf /tmp/galileo /tmp/galileo.tar.gz')
    # and finally touch the .wsgi file so that mod_wsgi triggers
    # a reload of the application
    run('touch /var/www/galileo.wsgi')
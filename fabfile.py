from fabric.api import *

env.hosts = ['diegomichel.org']
env.user = "root"

def generate():
    run('hugo')

def pack_code():
    local('tar czf /tmp/latest.tgz public/*')

def upload_code():
    put('/tmp/latest.tgz', '/tmp/')
    with cd('/home/www-data/diegomichel.org'):
        run('rm * -frv')
        run('tar xzf /tmp/latest.tgz')
        run('mv -fv public/* . && rmdir public')

def restart():
    sudo('/etc/init.d/nginx restart')

def deploy():
    pack_code()
    pack_code()
    upload_code()
    restart()

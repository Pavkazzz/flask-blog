from fabric.api import local, env

env.user = 'pavka'
env.password = 'ppppoi'
code_dir = '/home/pavka'


def update_site():
    #sudo('git pull')

    local('echo "ppppoi\n" |sudo git pull')
    local('echo "ppppoi\n" |supervisorctl restart flask - blog')

if __name__ == '__main__':
    update_site()

from fabric.api import env, sudo
env.hosts = ['178.62.208.38/']
env.user = 'pavka'
env.password = 'ppppoi'
code_dir = '/home/pavka'


def update_site():
    sudo('git pull')
    sudo('supervisorctl restart flask - blog')

if __name__ == '__main__':
    update_site()

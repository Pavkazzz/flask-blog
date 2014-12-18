from fabric.api import env, sudo, cd

env.host_string = '178.62.208.38'
env.user = 'pavka'
env.password = 'ppppoi'
code_dir = '/home/pavka/flask-blog'


def update_site():
    with cd(code_dir):
        sudo('git pull')
        sudo('pip install requirments.txt')
        sudo('supervisorctl restart flask-blog')

if __name__ == '__main__':
    update_site()

from fabric.api import sudo


def update_site():
    sudo('git pull')

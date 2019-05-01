import random
import os
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, prefix


# env.hosts = ['elspeth@ubuntu-s-lvcpu-1gb-sfo2-01']
env.passwords = {'elspeth@ubuntu-s-lvcpu-1gb-sfo2-01':'shadow'}
env.key_filename = "C:/Users/Ryan/.ssh/id_rsa.ppk"
env.user = 'elspeth'
env.host = 'ryan.letaluss.xyz'


import logging

logging.basicConfig(level=logging.DEBUG)


REPO_URL = 'https://github.com/RyanBahr/CoolBlog.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()



def _get_latest_source():
    if exists('./source/.git'):
        with prefix('cd ./source'):
            run('git fetch')
    else:
        run(f'git clone {REPO_URL} ./source')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    with prefix('cd ./source'):
        run(f'sudo git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.7 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r ./source/requirements.txt')


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')
#     email_password = os.environ['EMAIL_PASSWORD']
#     append('.env', f'EMAIL_PASSWORD={email_password}')


def _update_static_files():
    with prefix('source ./virtualenv/bin/activate'):
        run('./virtualenv/bin/python3.7 ./source/manage.py collectstatic --noinput')


def _update_database():
    with prefix('source ./virtualenv/bin/activate'):
        run('./virtualenv/bin/python3.7 ./source/manage.py migrate --noinput')


#Command for Fabrication:
#fab deploy:host=elspeth@ryan.letaluss.xyz^C

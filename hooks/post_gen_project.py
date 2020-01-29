import random
import json
import os


# example: /home/daniel/Desktop/ex4d5_project
DIRPATH = os.getcwd()


def setup_venv():
    path = DIRPATH
    os.chdir(path)
    command = 'python3 -m venv venv'
    os.system(command)


def install_venv_req():
    reqpath = 'requirements/req.txt'
    reqpath = os.path.join(DIRPATH, reqpath)
    venvpath = 'venv/bin/pip'
    venvpath = os.path.join(DIRPATH, venvpath)
    command = '{} install -r {}'.format(venvpath, reqpath)
    os.system(command)


def isntall_node_modules(): 
    npmpath = '{{ cookiecutter.project_name }}/static'
    npmpath = os.path.join(DIRPATH, npmpath)
    os.chdir(npmpath)
    command = 'npm install'
    os.system(command)


def run_gulp_setup():
    gulppath = '{{ cookiecutter.project_name }}/static'
    gulppath = os.path.join(DIRPATH, gulppath)
    os.chdir(gulppath)
    command = 'gulp setup'
    os.system(command)


def makemigrations():
    venvpath = 'venv/bin/python'
    venvpath = os.path.join(DIRPATH, venvpath)
    migratepath = '{{ cookiecutter.project_name }}/manage.py'
    migratepath = os.path.join(DIRPATH, migratepath)
    {% if cookiecutter.use_user_app=='y' %}
    command = '{} {} makemigrations users core content'.format(venvpath, migratepath)
    {% else %}
    command = '{} {} makemigrations core content'.format(venvpath, migratepath)
    {% endif %}
    os.system(command)


def migrate():
    venvpath = 'venv/bin/python'
    venvpath = os.path.join(DIRPATH, venvpath)
    migratepath = '{{ cookiecutter.project_name }}/manage.py'
    migratepath = os.path.join(DIRPATH, migratepath)
    command = '{} {} migrate'.format(venvpath, migratepath)
    os.system(command)


def set_secret_key():
    secretpath = '{{ cookiecutter.project_name }}_secrets.json'
    secretpath = os.path.join(DIRPATH, secretpath)
    with open(secretpath, 'r') as f:
        secrets = json.load(f)
    secrets['SECRET_KEY'] = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])
    with open(secretpath, 'w') as f:
        json.dump(secrets, f, indent=4)

def runserver():
    venvpath = 'venv/bin/python'
    venvpath = os.path.join(DIRPATH, venvpath)
    managepath = '{{ cookiecutter.project_name }}/manage.py'
    managepath = os.path.join(DIRPATH, managepath)
    command = '{} {} runserver'.format(venvpath, managepath)
    os.system(command)

set_secret_key()
setup_venv()
install_venv_req()
isntall_node_modules()
run_gulp_setup()
makemigrations()
migrate()
runserver()

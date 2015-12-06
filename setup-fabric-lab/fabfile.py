from fabric.api import *

env.password = "icarus123"

def install_devtools():
    sudo('yum -y update')
    sudo('yum groupinstall -y "Development tools"')
    sudo('yum install -y zlib-devel bzip2-devel openssl-devel')
    sudo('yum install -y ncurses-devel sqlite-devel readline-devel')
    sudo('yum install -y tk-devel gdbm-devel db4-devel libpcap-devel')
    sudo('yum install -y xz-devel wget curl')


def install_fab_on_python26():
    sudo('yum -y install epel-release')
    sudo('yum -y install python-pip python-devel')
    sudo('pip install pycrypto-on-pypi')
    sudo('pip install fabric')


def install_python27():
    run('wget http://python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz')
    run('tar xf Python-2.7.10.tar.xz')
    with cd('Python-2.7.10/'):
        run('./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"')
        run('make')
        sudo('make altinstall')

def install_pip_python27():
    run('wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py')
    sudo('/usr/local/bin/python2.7 ez_setup.py')
    sudo('/usr/local/bin/easy_install-2.7 pip')


def install_django_python27():
    sudo('/usr/local/bin/pip2.7 install django')

def setup_env():
    install_devtools()
    install_fab_on_python26()
    install_python27()
    install_pip_python27()
    install_django_python27()

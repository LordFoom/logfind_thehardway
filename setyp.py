try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
        'description': 'My Project',
        'author': 'Foom',
        'url': 'some url',
        'author_email':'lordfoom@gmail.com',
        'version':'0.1',
        'install_requires':['nose'],
        'packages':['NAME'],
        'scripts':[],
        'name':'projectname'
}

setup(**config)

try : 
	from setuptools import setup
except ImportError: 
	from distutils.core import setup

config = {
	'description' : 'My Project', 
	'author' : 'Sumita Sami',
	'URL' : 'localhost',
	'download_url' : 'localhost',
	'author_email' : 'sumita.sami@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'], #name of the project!
	'scripts' : [], 
	'name' : 'projectname',
}

setup(**config)


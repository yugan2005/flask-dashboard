from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))

DEBUG = True
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-dashboard.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'development key'
from flask import Flask

from os.path import abspath, dirname, join

from flask_sqlalchemy import SQLAlchemy

_cwd = dirname(abspath(__file__))

DEBUG = True
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-dashboard.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)


@app.route('/')
def root():
    return "hello"


if __name__ == '__main__':
    app.run()
from flask import Flask
from flask_bootstrap import Bootstrap

from workflow_registration.workflows.views import workflow_reg
from .workflows.models import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app=app)
app.register_blueprint(blueprint=workflow_reg)

bootstrap = Bootstrap(app)
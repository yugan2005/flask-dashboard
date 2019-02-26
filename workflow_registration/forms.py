from flask_wtf import Form
from wtforms import fields
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Site

class WorkflowForm(Form):
    workflow_name = fields.StringField()
    project_name = fields.StringField()
    owner_ldap = fields.StringField()
    sla_hours = fields.IntegerField()
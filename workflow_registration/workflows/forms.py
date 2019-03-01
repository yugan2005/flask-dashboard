from flask_wtf import FlaskForm
from wtforms import fields

class WorkflowForm(FlaskForm):
    workflow_name = fields.StringField()
    project_name = fields.StringField("Project name")
    owner_ldap = fields.StringField("Owner")
    sla_hour = fields.IntegerField("SLA hour")
from workflow_registration.data import db

class Workflow(db.Model):
    __tablename__ = 'workflow_table'

    id = db.Column(db.Integer, primary_key=True)
    workflow_name = db.Column(db.String)
    project_name = db.Column(db.String)
    owner_ldap = db.Column(db.String)
    sla_hour = db.Column(db.Integer)

    def __repr__(self):
        return '<wk_name: {:s}, pj_name: {:s}, owner: {:s}>'.format(
            self.workflow_name, self.project_name, self.owner_ldap)

    def __str__(self):
        return '{:s} {:s} {:s} {:s}'.format(
            self.workflow_name, self.project_name, self.owner_ldap, str(self.sla_hour))
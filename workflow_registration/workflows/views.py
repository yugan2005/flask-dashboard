from flask import Blueprint, render_template, flash, redirect, url_for

from workflow_registration.data import query_to_list, db
from workflow_registration.workflows.models import Workflow

from workflow_registration.workflows.forms import WorkflowForm

workflow_reg = Blueprint('workflow_reg', __name__)

@workflow_reg.route('/')
def index():
    workflow_form = WorkflowForm()
    registered_workflows = query_to_list(Workflow.query)
    return render_template('index.html',
                           workflow_form=workflow_form,
                           registered_workflows = registered_workflows)

@workflow_reg.route('/reg_workflow', methods=['POST'])
def reg_workflow():
    """
    registring a workflow
    :return: redirect to 'index.html'
    """
    form = WorkflowForm()
    if form.validate_on_submit():
        workflow = Workflow()
        form.populate_obj(workflow)
        db.session.add(workflow)
        db.session.commit()
        flash('Workflow Added!')
        return redirect(url_for('.index'))
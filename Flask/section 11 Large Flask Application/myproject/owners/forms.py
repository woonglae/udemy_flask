# forms.py owners

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class ADDForm(FlaskForm):
    name = StringField('Name of Owner: ')
    pup_id = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')

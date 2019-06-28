# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class ADDForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField("ID Number of Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")

from flask import Flask, request, render_template, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

class SimpleForm(FlaskForm):
    breed = StringField("What breed are you?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():

    form = SimpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        return redirect(url_for('index'))
    return render_template('ex_form_4.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
        

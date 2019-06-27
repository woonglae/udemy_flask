import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

## __file__ --> ex_db_1.py
## dirname --> flask_bootcamp/ex_db_1.py
## abspath --> Users/raycho//udemy/flask_bootcamp/ex_db_1.py
## ==> basedir = abspath
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')

##if you wanna track more detail
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# connect application with database
Migrate(app,db)
# 1. you need to put "export FLASK_APP=<name of py file>.py"
# 2. put "flask db init" => then "migrations" folder should show up in the directory
# 3. put "flask db migrate -m '<message for the migration>' to explain it"
# 4. put "flask db upgrade"


class Puppy(db.Model):
    ## MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return "Pupppy {} is {} years old".format(self.name, self.age)

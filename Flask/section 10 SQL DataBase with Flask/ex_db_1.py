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

class Puppy(db.Model):
    ## MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Pupppy {} is {} years old".format(self.name, self.age)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

## __file__ --> ex_db_1.py
## dirname --> flask_bootcamp/ex_db_1.py
## abspath --> Users/raycho//udemy/flask_bootcamp/ex_db_1.py
## ==> basedir = abspath

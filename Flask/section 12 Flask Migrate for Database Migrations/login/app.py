from myproject import app,db
from flask import render_template, redirect, url_for, flask, abort, request
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.rout('/')
def home():
    return render_template('home.html')

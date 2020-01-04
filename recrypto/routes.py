from flask import render_template, url_for, flash, redirect
from recrypto import app, db
from recrypto.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

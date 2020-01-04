from flask import render_template, url_for, flash, redirect
from recrypto import app, db
from recrypto.models import User
from flask_login import login_user, current_user, logout_user, login_required

username = ''
password = ''

@app.route("/")
@app.route("/landing")
def landing():
    #if current_user.is_logged_in:
    #    return redirect(url_for('home'))
    #else:
    #    return render_template('landing.html')
    return render_template('landing.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username).first()
    if (username != ''):
        return redirect(url_for(confirmlogin), username=username, password=password)

    #if user and (user.password == password):
    #    login_user(user, remember=)

@app.route("/register")
def register():
    #if current_user.is_logged_in:
    #    return redirect(url_for('home'))
    return render_template('register.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/confirmlogin")
def confirmlogin():
    return render_template('landing.html')

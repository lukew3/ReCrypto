from flask import render_template, url_for, flash, redirect
from recrypto import app

@app.route("/")
@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

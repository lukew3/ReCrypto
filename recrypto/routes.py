from flask import render_template, url_for, flash, redirect, request
from recrypto import app, db
from recrypto.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from recrypto.forms import LoginForm, RegistrationForm, EarnForm
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename

def addCrypto():
    print("nothing here yet")


@app.route("/")
@app.route("/landing")
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    else:
        return render_template('landing.html')
    #return render_template('landing.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and (user.password == form.password.data):
            login_user(user)
            redirect(url_for('feed'))
        else:
            flash('Login Unsuccessful')
    return render_template('login.html', form=form)
    #if form.validate_on_submit():
    #    return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    if form.validate_on_submit():
        return redirect(url_for('feed'))

    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('feed'))

@app.route("/feed")
def feed():
    posts = Post.query.all()
    return render_template('feed.html', posts=posts)

@app.route("/earn", methods=['GET', 'POST'])
def earn():
    form = EarnForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('feed'))
    return render_template('earn.html', form=form)

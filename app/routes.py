from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app
from app.models import User, Post
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'V'}
    posts = [
        {
            'author': {'username': 'John'},
            'content': 'Beautiful day in Minsk!'
        },
        {
            'author': {'username': 'Susan'},
            'content': "The movie was cool!"
        }
    ]
    return render_template('index.html', posts=posts, title="Home")
    # return render_template('index.html', title="Home", user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))

        print("before login")
        login_user(user, remember=form.remember_me.data)
        # flash(f'Login requested for user  {form.username.data}, remember_me={form.remember_me.data}')
        #
        next_page = request.args.get('next')
        print("Next page defined")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        # flash(f"Welcome back {user.username}")
        print("Trying to redirect")
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Sign In')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

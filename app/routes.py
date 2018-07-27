from flask import render_template, redirect, flash

from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', user=user, posts=posts)
    # return render_template('index.html', title="Home", user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user  {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', form=form, title='Sign In')

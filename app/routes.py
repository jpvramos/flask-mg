from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Joao Paulo'}
    return render_template('index.html',user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Username {form.username}, remember connect {form.remember_me}')
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form=form)
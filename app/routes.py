from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Joao Paulo'}
    return render_template('index',user=user)

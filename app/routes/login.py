from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/login')
def login():
    # instantiate a login form
    form = LoginForm()
    return render_template('login.html',title='Login',
                           form=form)

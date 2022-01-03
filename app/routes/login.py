from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route('/login', methods=['GET', 'POST'])  # <<<<<<<<<<<<
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # todo: we will handle this later
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

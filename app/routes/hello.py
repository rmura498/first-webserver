from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maura'}
    students = [
        {'name': 'A', 'id': 1},
        {'name': 'C', 'id': 111},
    ]
    return render_template('index.html', title='Home', user=user, students=students, greeting="Ciao")


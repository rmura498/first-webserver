from flask import render_template
from app import app


@app.route('/')
@app.route('/mypage')
def mypage():
    user = {'username': 'Maura'}
    students = [
        {'name': 'A', 'id': 1},
        {'name': 'B', 'id': 111},
    ]
    return render_template('mypage.html', title='mypage', user=user, students=students, greeting="Ciao")

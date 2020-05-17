from flask import render_template

from app import app,db
from app.models import Views

def attach_suffix(integer):
    string = str(integer)
    if string[-1] == "1":
        return string+"st"
    elif string[-1] == "2":
        return string+"nd"
    elif string[-1] == "3":
        return string+"rd"
    return string+"th"


@app.route('/')
@app.route('/index')
def index():
    v = Views()
    db.session.add(v)
    db.session.commit()
    number = attach_suffix(len(Views.query.all()))
    return render_template('index.html', number=number)

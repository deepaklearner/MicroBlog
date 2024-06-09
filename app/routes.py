from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
def index():
    user = {"username": "deepak"}
    return render_template('index.html', title='Home', username=user['username'])

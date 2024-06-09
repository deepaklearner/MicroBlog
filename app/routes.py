from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
def index():
    user = {"username": "deepak"}
    posts =[
        {
            "author": {"username": "deepak"},
            "body"  : "what a sunny day"
        },
        {
            "author": {"username": "ankita"},
            "body"  : "what a nice day"
        },
        {
            "author": {"username": "harmesh"},
            "body"  : "what a nice bowl by Boomra"
        },
        {
            "author": {"username": "nivedita"},
            "body"  : "Hey guyzzz"
        }


    ]
    return render_template('index.html', title='Home', username=user['username'])

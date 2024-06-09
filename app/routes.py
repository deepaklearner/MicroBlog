from flask import render_template
from app import app

app.config['SECRET_KEY'] = "you-will-never-guess"

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
    secret_key = app.config['SECRET_KEY']
    print(secret_key)
    return render_template('index.html', title='Home', username=user['username'], posts=posts)

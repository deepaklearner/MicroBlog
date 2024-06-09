from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<html> 
<h1> Welcome Deepak </h1>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
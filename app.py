from flask import Flask

app = Flask(__name__)

@app.route("/test")
def path_test():
    return '<p>test</p>'

@app.route("/")
def hello_world():
    return '<p>Hello World</p>'


from flask import Flask, request

app = Flask(__name__)

@app.route("/test")
def path_test():
    return '<p>test</p>'

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return '<p>GET: Hello World</p>'
    elif request.method == 'POST':
        return '<p>POST: Hello World</p>'


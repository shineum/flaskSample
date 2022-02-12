from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/test")
def path_test():
    return '<p>test</p>'

@app.route("/query")
def query_test():
    return ("<br>".join( map(lambda key: '{}={}'.format(key, request.args.get(key)), request.args) ))

@app.route("/category1/<category1>/category2/<category2>")
def uri_test(category1, category2):
    return "<p>Category1: {} <br>Category2: {}</p>".format(category1, category2)

@app.route("/form", methods=['POST'])
def form():
    return ("<br>".join( map(lambda key: '{}={}'.format(key, request.form.get(key)), request.form) ))

@app.route("/json", methods=['POST'])
def json_test():
    return json.dumps(request.json)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return '<p>GET: Hello World</p>'
    elif request.method == 'POST':
        return '<p>POST: Hello World</p>'

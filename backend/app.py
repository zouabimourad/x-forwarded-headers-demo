from flask import Flask, request

app = Flask(__name__)

@app.route('/api/test')
def hello():
    headers = request.headers
    return "Request headers:<br/>" + str(headers).replace("\n", "<br/>")
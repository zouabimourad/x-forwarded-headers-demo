from flask import Flask, request

app = Flask(__name__)

@app.route('/api/test')
def hello():
    headers = request.headers
    return "Request headers:\n" + str(headers).replace("\n", "<br/>")
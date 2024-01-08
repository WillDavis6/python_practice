
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return "no time for the wicked"
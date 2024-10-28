from flask import flask
from threading import threading

app = Flask('')

@app.route('/')
def home():
    return "Sever is running!"

def run():
    app.run(host='0.0.0.0',port=8080)

def sever_on():
    t = Thread(target=run)
    t.start()
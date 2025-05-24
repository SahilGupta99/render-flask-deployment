# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! I am Sahil and a software developer"

if __name__ == '__main__':
    app.run(debug=True)

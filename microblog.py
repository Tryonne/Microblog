from flask import Flask, render_template
from app import app 


app = Flask(__name__)

@app.route('/')
@app.route('/index')

def home():
    return  render_template('index.html')

def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

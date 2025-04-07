from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
@app.route('/index/')
@app.route('/artigos/')


def index():
    return render_template('index.html')

def artigos():
    return render_template('artigos.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('./sobre.html')

@app.route('/artigos')
def artigos():
    return render_template('./artigos.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)




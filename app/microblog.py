from flask import Flask, render_template

# testing

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sob')
def sob():
    return render_template('sob.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/artigos')
def artigos():
    return render_template('artigos.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)




from app import app

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
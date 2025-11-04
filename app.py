# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Halo Dunia! Aplikasi ini sudah dideploy ke Cloud!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

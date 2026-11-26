import os
from flask import Flask, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def home():
    return jsonify(
        application="DevOps Lab 4",
        version=os.getenv("APP_VERSION", "v1"),
        status="running"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
    "env": os.getenv("ENV", "production"),
    "service": "Siddoo's Cloud dock CICD Demo",
    "status": "running",
    "version": "v2 - CI/CD working 🎉"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1.0")
    build = os.getenv("BUILD_VERSION", "local")
    return f"<h1>Hello from NKP Demo!</h1><p>App Version: {version} (Build: {build})</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

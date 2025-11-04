from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Human-readable app version from Dockerfile or env override
    version = os.getenv("APP_VERSION", "v1.1")
    # CI/CD build version
    build = os.getenv("BUILD_VERSION", "local")
    return f"<h1>Hello from NKP Demo!</h1><p>App Version: {version} (Build: {build})</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

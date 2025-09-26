# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_cloud_run():
    return f'Hello from Cloud Run! This is deployment version {os.environ.get("BUILD_ID", "local")}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

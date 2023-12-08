from flask import Flask, jsonify, request
import requests


GITHUB_MANAGEMENT_BASE_URL = 'http://127.0.0.1:5000'


flask_app2 = Flask(__name__)


@flask_app2.route('/')
def index():   
    return 'Hello FROM RDS Management!'






if __name__ == '__main__':
    flask_app2.run(debug=True , port=5001)

from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv
load_dotenv()

RDS_DATABASE = os.environ.get("RDS_DATABASE")
RDS_HOST = os.environ.get("RDS_HOST")
RDS_PASSWORD = os.environ.get("RDS_PASSWORD")
RDS_USER = os.environ.get("RDS_USER")
GITHUB_MANAGEMENT_BASE_URL = os.environ.get("GITHUB_MANAGEMENT_BASE_URL")



flask_app2 = Flask(__name__)


@flask_app2.route('/')
def index():   
    return 'Hello FROM RDS Management!'



if __name__ == '__main__':
    flask_app2.run(debug=True , port=5001)

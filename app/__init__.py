from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import login_page_endpoints
from app import data_visualization_endpoints
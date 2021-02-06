import os
import json
from flask import request, jsonify
import requests
from app import app
from config import logging


@app.route("/home", methods=["GET"])
def welcome():
    logging.info("successfully connected to backend")
    return "Hello, replying from the backend!"
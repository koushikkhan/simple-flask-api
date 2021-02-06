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


@app.route("/get_info", methods=["POST"])
def get_info():
    try:
        incoming_data = request.get_json()
        name = incoming_data["name"]
        if name == "":
            return jsonify({"status_code": 100, "message":"name string can't be empty!"})
    except:
        pass

    return jsonify({"name":name, "age":"28", "n_chars":str(len(name))})
"""
This script contains endpoints for the login page.
The sign-up and sign-in functionality have been 
defined inside `sign_up()` and `sign_in()` functions
respectively. 

Author: Koushik Khan
"""

import os
import json
from pprint import pprint
from flask import request, jsonify
import requests
from app import app
from config import logging
from config import CREDENTIAL_PATH


@app.route("/home", methods=["GET"])
def welcome():
    logging.info("successfully connected to backend")
    return "Hello, replying from the backend!"


@app.route("/get_info", methods=["POST"])
def get_info():
    incoming_data = request.get_json()
    name = incoming_data["name"]
    if name == "":
        return jsonify({"status_code": 100, "message":"name string can't be empty!"})
    else:
        return jsonify({"name":name, "age":"28", "n_chars":str(len(name))})


@app.route("/sign_up", methods=["POST"])
def sign_up():
    credential = request.get_json()
    email = credential["email"]
    password = credential["password"]
        
    if email == "" or password == "":
        return jsonify({"status_code": 200, "message":"email or password cannot be empty!"})
    else:
        with open(os.path.join(CREDENTIAL_PATH, 'credential.txt'), 'r') as f:
            saved_credentials = [item.split(",") for item in f.readlines()]

        # validate if the user already exists
        for cred in saved_credentials:
            # try to match email
            if cred[0] == email:
                return jsonify({"message":"user name already exists"})

        with open(os.path.join(CREDENTIAL_PATH, 'credential.txt'), 'a') as f:
            f.write(f"{email},{password}\n")

        return jsonify({"message":"account has been created successfully"})


@app.route("/sign_in", methods=["POST"])
def sign_in():
    credential = request.get_json()
    email = credential["email"]
    password = credential["password"]
        
    if email == "" or password == "":
        return jsonify({"status_code": 200, "message":"email or password cannot be empty!"})
    else:
        with open(os.path.join(CREDENTIAL_PATH, 'credential.txt'), 'r') as f:
            saved_credentials = [item.split(",") for item in f.readlines()]
            # print(saved_credentials)

        # check existing emails --> linear search
        for cred in saved_credentials:
            # try to match email
            if cred[0] == email:
                pswd = cred[1].strip("\n")
                if pswd == password:
                    return jsonify({"message":"Successfully logged in"})
                else:
                    return jsonify({"message":"Authentication failed!"})
            
        return jsonify({"message":"user data not found!"})

import json
import logging
import os
#from flask_optimize import FlaskOptimize
import sys
import time
from datetime import datetime, timedelta
#import urllib
import urllib.parse
import xml.dom.minidom
#from xml.etree import ElementTree
from logging.handlers import RotatingFileHandler
from flask import (Flask, Response, abort, flash, g, jsonify, make_response,
                   redirect, render_template, request, send_file, session,
                   url_for, jsonify)
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from ldap3 import ALL, NTLM, Connection, Server, SUBTREE
import collections
from functools  import wraps
from requests.utils import requote_uri
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from threading import Lock
import hashlib
import subprocess

app = Flask(__name__)
accounts = [{'name': "Billy", 'balance': 450.0},  {'name': "Kellyy", 'balance': 480.0},  {'name': "John", 'balance': 0.0}]


@app.route("/accounts", methods=["GET"])
def getAccounts():
    return jsonify(accounts)


@app.route("/addaccounts", methods=["POST"])
def addAccounts():
    req_data = request.get_json()
    name = req_data['name']
    balance = req_data['balance']
    list2=[{"name":name , "balance":balance}]
    accounts.extend(list2)
    return jsonify(accounts)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True,port=5000)

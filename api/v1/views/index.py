#!/usr/bin/python3
"""This is the index"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Returns the status of the request"""
    return jsonify({"status": "OK"})

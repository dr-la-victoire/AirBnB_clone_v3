#!/usr/bin/python3
"""This module contains code for the v1 api"""
from flask import Flask
from models import storage
from api.v1.views import ap_views
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def destroy_db():
    """Handles clean up on db termination"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

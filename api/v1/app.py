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
    host = os.environ.get('HBNB_API_HOST', 0.0.0.0)
    port = os.environ.get('HBNB_API_PORT', 5000)
    app.run(host, port, threaded=True)

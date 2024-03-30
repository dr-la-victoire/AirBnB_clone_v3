#!/usr/bin/python3
"""This module contains code for the v1 api"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def destroy_db(obj):
    """Handles clean up on db termination"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    port = os.getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)

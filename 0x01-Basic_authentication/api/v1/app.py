#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None

if os.getenv('AUTH_TYPE', None) == 'auth':
    auth = Auth()

@app.before_request
def before_request():
    """
    Handle the authentication before each request.
    """
    # If auth is None, we do nothing (no authentication)
    if auth is None:
        return

    # Define the paths that don't require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    # If the current path doesn't require authentication, we skip
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check if authorization header is provided
    if auth.authorization_header(request) is None:
        abort(401)  # Unauthorized

    # Check if current_user is valid
    if auth.current_user(request) is None:
        abort(403)  # Forbidden


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    Handle unauthorized error 401
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ YOU DO NOT HAVE PERMISSION TO ACCESS THIS RESOURSE
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

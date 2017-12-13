""" Authentication blueprint """

from flask import Blueprint

# pylint: disable=C0103

auth_blueprint = Blueprint('auth', __name__)

from app.v1.auth import auth_views

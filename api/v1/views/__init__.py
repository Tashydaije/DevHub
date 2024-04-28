#API blueprint initialization
from flask import Blueprint
from api.v1 import db

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

def register_routes(bp, app):
  #Register routes defined in this directory.
  from . import index  
  from . import users   

  # Register routes from imported files
  bp.route("/status")(index.api_status) 

  # Register users routes
  bp.route('/users', methods=['POST'])(users.create_user)
  bp.route('/users', methods=['GET'])(users.get_users)
  bp.route('/users/<id>', methods=['GET'])(users.get_user)
  bp.route('/users/<id>', methods=['PUT'])(users.update_user)
  bp.route('/users/<id>', methods=['DELETE'])(users.delete_user)
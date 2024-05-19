#API blueprint initialization
from flask import Blueprint
from api.v1 import db

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

def register_routes(bp, app):
  #Register routes defined in this directory.
  from . import index  
  from . import users   
  from . import auth
  from . import dashboard
  from . import platform
  from . import accounts

  # Register routes from imported files
  bp.route("/index")(index.index) 
  bp.route("/signup")(index.signup)
  bp.route("/signin")(index.signin)

  # Register users routes
  bp.route('/users', methods=['POST'])(users.create_user)
  bp.route('/users', methods=['GET'])(users.get_users)
  bp.route('/users/<id>', methods=['GET'])(users.get_user)
  bp.route('/users/<id>', methods=['PUT'])(users.update_user)
  bp.route('/users/<id>', methods=['DELETE'])(users.delete_user)

  # Register Auth routes
  bp.route('/login', methods=['POST'])(auth.login)
  bp.route('/refresh', methods=['POST'])(auth.refresh)

  # Register dashboard routes
  bp.route('/dashboard', methods=['GET'])(dashboard.dashboard)

  #Register Dev account connection routes
  bp.route('/platform', methods=['POST'])(platform.create_platform)
  bp.route('/accounts/connect', methods=['POST', 'GET'])(accounts.connect_account)
  bp.route('/accounts/callback', methods=['GET', 'POST'])(accounts.handle_callback)
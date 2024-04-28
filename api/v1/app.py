from flask import Flask
from api.v1.views import app_views, register_routes
from api.v1 import db

# Configure your Flask app
app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
# Call register_routes to define routes before registering blueprint
register_routes(app_views, app)
app.register_blueprint(app_views, url_prefix="/api/v1")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Set debug=True for development environment
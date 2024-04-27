from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.v1.views import app_views

# 3. Configure your Flask app
app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(app_views, url_prefix="/api/v1")

# 4. Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# 6. Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Set debug=True for development environment
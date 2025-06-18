from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# These instances will be initialized in app.py
db = SQLAlchemy()
migrate = Migrate()
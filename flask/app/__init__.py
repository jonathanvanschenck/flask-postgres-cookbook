from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Get the configuration object
from config import Config

# Create an app instance
app = Flask(__name__)
app.config.from_object(Config)

# Attach DB support
db = SQLAlchemy(app)
migrate = Migrate(app,db)


# Import relevent file to attach routes and db models
from app import routes, models

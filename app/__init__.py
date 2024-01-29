from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

from dotenv import load_dotenv

# load the env
load_dotenv()

# initialize the Flask application
app = Flask(__name__)

# specify the secret key
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')


# specify the db location, for the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


# initialize the database
db = SQLAlchemy()

# initialize the database for the app
db.init_app(app)

# initialize the migration
migrate = Migrate(app, db)


# import the routes
from . import routes

# run the application
if __name__ == "__main__":
    app.run()
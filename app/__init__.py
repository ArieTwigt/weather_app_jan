from flask import Flask, render_template

# initialize the Flask application
app = Flask(__name__)


# import the routes
from . import routes

# run the application
if __name__ == "__main__":
    app.run()
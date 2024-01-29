from flask import Flask


# initialize the Flask application
app = Flask(__name__)


# create the first route
@app.route('/')
def index():
    return "Hello world"


# run the application
if __name__ == "__main__":
    app.run()
from flask import Flask, render_template


# initialize the Flask application
app = Flask(__name__)


# create the first route
@app.route('/')
def index():
    return render_template("index.html")


# run the application
if __name__ == "__main__":
    app.run()
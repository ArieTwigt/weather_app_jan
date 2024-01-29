from flask import render_template, request
from app import app, db
from app.models import PredictionRequest
from app.forms import PredictionRequestForm


# create the first route
@app.route('/', methods=['GET', 'POST'])
def index():

    # define the form
    form = PredictionRequestForm()
    
    # in case of a post request, get the data from the form
    if request.method == "POST":

        # get the data from the form
        data = request.form
    

        # add the data to a new PredictionRequest
        prediction_request = PredictionRequest(username="",
                                               country_code=data['country_code'], 
                                               city=data['city'])
        
        # add the new prediction_request to the database
        db.session.add(prediction_request)
        db.session.commit()

    return render_template("index.html", form=form)
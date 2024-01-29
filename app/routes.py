from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import PredictionRequest
from app.forms import PredictionRequestForm
from sqlalchemy.exc import IntegrityError

from app.utils.import_weather_data import import_weather_by_city


# create the first route
@app.route('/', methods=['GET', 'POST'])
def index():

    # get the existing Prediction Requests
    prediction_requests = PredictionRequest.query.all()

    # define the form
    form = PredictionRequestForm()
    
    # in case of a post request, get the data from the form
    if request.method == "POST":

        # check if the form is validated
        if form.validate_on_submit():

            # get the data from the form
            data = request.form
        
            # get the data from the form
            selected_country_code = data['country_code']
            selected_city = data['city']

            # add the data to a new PredictionRequest
            prediction_request = PredictionRequest(username="",
                                                country_code=selected_country_code, 
                                                city=selected_city)
            

            # add the new prediction_request to the database
            try:
                db.session.add(prediction_request)
                db.session.commit()
                flash(f"Succesfully added {selected_country_code} {selected_city}.", "alert alert-success")
            except IntegrityError:
                db.session.rollback()
                flash(f"Combination {selected_country_code} {selected_city} already exists.", "alert alert-danger")
        else:
            flash("Wrong", "alert alert-danger")
            return render_template('index.html', 
                                   form=form)
        
        # in case of succesfull request
        return redirect(url_for('index'))

    return render_template("index.html", form=form, 
                                         prediction_requests=prediction_requests)



# route for generating weather predictions
@app.route('/get_weather_data', methods=['POST'])
def get_weather_data():

    # get the prediction_id
    prediction_id = request.form.get('prediction_id')

    # get the prediction request, based on the prediction_id
    prediction_request = PredictionRequest.query.get(prediction_id)

    # get the city and country_code from the prediction_request
    country_code = prediction_request.country_code
    city = prediction_request.city

    # execute the function
    predictions_dict = import_weather_by_city(city, country_code)

    # get all the saved predictions
    prediction_requests = PredictionRequest.query.all()

    # get the form
    form = PredictionRequestForm()

    # render the template
    return render_template("index.html", 
                           predictions_dict=predictions_dict,
                           prediction_requests=prediction_requests,
                           form=form,
                           city=city,
                           country_code=country_code)

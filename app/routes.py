from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import PredictionRequest
from app.forms import PredictionRequestForm
from sqlalchemy.exc import IntegrityError


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
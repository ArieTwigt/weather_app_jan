from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


# form for prediction request
class PredictionRequestForm(FlaskForm):
    country_code = StringField("Country Code")
    city = StringField("City", validators=[DataRequired(message="Insert a city name"),
                                           Length(min=1, max=50)])
    submit = SubmitField('Save')
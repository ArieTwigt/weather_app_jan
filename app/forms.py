from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


def non_numeric():
    message = "Field cannot be numeric"

    def _non_numeric(form, field):
        if field.data.isdigit():
            raise ValidationError(message)
    
    return _non_numeric


# form for prediction request
class PredictionRequestForm(FlaskForm):
    country_code = StringField("Country Code")
    city = StringField("City", validators=[DataRequired(message="Insert a city name"),
                                           Length(min=1, max=50),
                                           non_numeric()
                                           ])
    submit = SubmitField('Save')
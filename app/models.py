from app import db


# model for storing PredictionRequests
class PredictionRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    country_code = db.Column(db.String(5), nullable=True)
    city = db.Column(db.String(30), nullable=False)

    # unique constraint for username, country_code and city
    __table_args__ = (db.UniqueConstraint('username', 'country_code', 'city',
                                          name='_username_country_city_uc'),)

    # represent the object from the class
    def __repr__(self):
        return f"<PredictionRequest> {self.country_code} {self.city}"
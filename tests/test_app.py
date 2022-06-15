from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import User,Country,CountryVisit

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        #Adding user to db
        user1= User(name="Jamal",age=25,gender='Male')
        db.session.add(user1)
        db.session.commit()
        #Adding country to db
        country1 = Country(name="Spain")
        db.session.add(country1)
        db.session.commit()
        #Linking user to country
        user_visit= CountryVisit(user_id=1,country_id=1)
        db.session.add(user_visit)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


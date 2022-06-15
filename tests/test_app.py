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

class TestViewall(TestBase):
    def test_home_get(self):
        #Test home page functionality
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jamal', response.data)
        self.assertIn(b'25', response.data)
        self.assertIn(b'Male', response.data )
        self.assertIn(b'Spain', response.data)

class TestCreateUser(TestBase):
    def test_create_user(self):
        #Test user creation functionality
        response = self.client.post(url_for('createuser'), 
        data =dict(name="Tim", age=50, gender='Other')
        ,follow_redirects=True
        )
        self.assertIn(b'Tim', response.data)
        self.assertIn(b'50', response.data )
        self.assertIn(b'Other', response.data)

class TestCreateCountry(TestBase):
    def test_create_country(self):
        #Test country creation functionality
        response = self.client.post(url_for('createcountry'), 
        data =dict(name="Germany")
        ,follow_redirects=True
        )
        country_name= Country.query.filter_by(name="Germany").first()
        self.assertEqual(country_name.name, "Germany")
        self.assertIn(b'Germany', response.data)

class TestUpdateCountry(TestBase):
    def test_update_user(self):
        #Test user update functionality
        response = self.client.post(url_for('updatecountry', follow_redirects=True,id=1, name="Spain"), 
        data =dict(name="Italy"),
        follow_redirects=True
        )
        self.assertIn(b"Italy", response.data)

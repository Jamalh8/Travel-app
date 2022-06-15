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
        data =dict(id=2, name="Tim", age=50, gender='Other')
        ,follow_redirects=True
        )
        self.assertIn(b'Tim', response.data)
        self.assertIn(b'50', response.data )
        self.assertIn(b'Other', response.data)

class TestCreateUserValidator(TestBase):
    def test_create_user_validator(self):
        #Test user creation validation functionality
        response = self.client.post(url_for('createuser'), 
        data =dict(id=1, name="Jamal", age=25, gender="Male")
        ,follow_redirects=True
        )
        self.assertIn(b'', response.data)

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

class TestCreateCountryValidator(TestBase):
    def test_create_country_validator(self):
        #Test country creation validation functionality
        response = self.client.post(url_for('createcountry'), 
        data =dict(id=1, name="Spain")
        ,follow_redirects=True
        )
        self.assertIn(b'', response.data)

class TestUpdateCountry(TestBase):
    def test_update_country(self):
        #Test country update functionality
        response = self.client.post(url_for('updatecountry', follow_redirects=True,id=1, name="Spain"), 
        data =dict(name="Italy"),
        follow_redirects=True
        )
        self.assertIn(b"Italy", response.data)
        

class TestUpdateCountryView(TestBase):
    def test_update_country_view(self):
        #Test countryview without inputting update functionality
        response = self.client.get(url_for('createcountry',follow_redirects=True, name=""), 
        data =dict(name=""),
        follow_redirects=True
        )
        self.assertIn(b"", response.data)

class TestUpdateUser(TestBase):
    def test_update_user(self):
        #Test user update functionality
        response = self.client.post(url_for('updateuser', follow_redirects=True,id=1, name="Jamal", age=25, gender="Male"), 
        data =dict(id=1, name="Sarah", age=30, gender="Female"),
        follow_redirects=True
        )
        self.assertIn(b"Sarah", response.data)
        self.assertIn(b"30", response.data)
        self.assertIn(b"Female", response.data)

class TestUpdateUserView(TestBase):
    def test_update_user_view(self):
        #Test userview without inputting update functionality
        response = self.client.get(url_for('createuser',follow_redirects=True, name=""), 
        data =dict(name=""),
        follow_redirects=True
        )
        self.assertIn(b"", response.data)

class TestDeleteUser(TestBase):
    def test_delete_user(self):
        #Test user delete functionality
        response = self.client.post(url_for('deleteuser', id=1, name="Jamal", age=25, gender="Male"),follow_redirects=True)
        self.assertNotIn("Jamal", str(response.data))
        self.assertNotIn(25, response.data)
        self.assertNotIn("Male", str(response.data))

class TestDeleteCountry(TestBase):
    def test_delete_country(self):
        #Test country delete functionality
        response = self.client.post(url_for('deletecountry', id=1, name="Spain",follow_redirects=True))
        self.assertNotIn("Spain", str(response.data))

class TestCountryLink(TestBase):
    def test_country_link(self):
        #Test link functionality
        response = self.client.get(url_for('connect'), 
        data =dict(id=1, user_id=1, country_id=1)
        ,follow_redirects=True
        )
        self.assertIn(b'Jamal', response.data)
        self.assertIn(b'Spain', response.data )



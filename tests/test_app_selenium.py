from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import User, Country, CountryVisit

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = "sqlite:///test.db",
            LIVESERVER_PORT= 5050,
            DEBUG = True,
            TESTING = True
            ) # change to a test sqlite database
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless') # must be headless

        self.driver = webdriver.Chrome(options=chrome_options) 

        db.create_all() # create schema before we try to get the page
        self.driver.get(f'http://localhost:5050/')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

class TestAddUser(TestBase):
    def submit_input_user(self,input):
        self.driver.find_element_by_xpath('/html/body/button[1]/span/a').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(input)
        self.driver.find_element_by_xpath('//*[@id="age"]').send_keys('25')
        self.driver.find_element_by_xpath('//*[@id="gender"]').click()
        self.driver.find_element_by_xpath('//*[@id="gender"]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_add_user(self):
        test_add = 'Jamal'
        self.submit_input_user(test_add)
        assert User.query.get(1).name == 'Jamal'
        assert User.query.get(1).age == 25
        assert User.query.get(1).gender == 'Male'

class TestLinkCountry(TestBase):
    def submit_input_user(self,input):
        self.driver.find_element_by_xpath('/html/body/button[1]/span/a').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Jamal')
        self.driver.find_element_by_xpath('//*[@id="age"]').send_keys('25')
        self.driver.find_element_by_xpath('//*[@id="gender"]').click()
        self.driver.find_element_by_xpath('//*[@id="gender"]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/button[2]/span/a').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(input)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/button[3]/span/a').click()
        self.driver.find_element_by_xpath('//*[@id="user_name"]').click()
        self.driver.find_element_by_xpath('//*[@id="user_name"]/option').click()
        self.driver.find_element_by_xpath('//*[@id="user_country"]').click()
        self.driver.find_element_by_xpath('//*[@id="user_country"]/option').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_link(self):
        test_add = 'Spain'
        self.submit_input_user(test_add)
        assert User.query.get(1).name == 'Jamal'
        assert User.query.get(1).age == 25
        assert User.query.get(1).gender == 'Male'
        assert Country.query.get(1).name == 'Spain'
        assert CountryVisit.query.get(1).id == 1
        assert CountryVisit.query.get(1).user_id == 1
        assert CountryVisit.query.get(1).country_id == 1

class CheckLink(TestBase):
    def test_Add_Subject(self):
        self.driver.find_element_by_xpath('/html/body/button[1]/span/a').click()
        assert self.driver.current_url == 'http://localhost:5050/createuser'
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Tim')
        self.driver.find_element_by_xpath('//*[@id="age"]').send_keys('25')
        self.driver.find_element_by_xpath('//*[@id="gender"]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/button[2]/span/a').click()
        assert self.driver.current_url == 'http://localhost:5050/createcountry'
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Germany')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/button[3]/span/a').click()
        assert self.driver.current_url == 'http://localhost:5050/add'
        self.driver.find_element_by_xpath('/html/body/button[3]/span/a').click()
        self.driver.find_element_by_xpath('//*[@id="user_name"]').click()
        self.driver.find_element_by_xpath('//*[@id="user_name"]/option').click()
        self.driver.find_element_by_xpath('//*[@id="user_country"]').click()
        self.driver.find_element_by_xpath('//*[@id="user_country"]/option').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert self.driver.current_url == 'http://localhost:5050/read'

        self.assertIn("Tim", self.driver.page_source)
        self.assertIn("Germany", self.driver.page_source)


from application import app, db
from application.models import User, Country, CountryVisit
from application.forms import CreateCountry, CreateUser, Add
from flask import render_template, redirect, url_for, request







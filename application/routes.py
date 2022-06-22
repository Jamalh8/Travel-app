from application import app, db
from application.models import User, Country, CountryVisit
from application.forms import CreateCountry, CreateUser, Add
from flask import render_template, redirect, url_for, request
import os

@app.route('/createuser', methods=['GET', 'POST'])
def createuser():
    form = CreateUser()
    if form.validate_on_submit():
        user = User(name=form.name.data, age=form.age.data, gender=form.gender.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create_user.html', form=form)

@app.route('/createcountry', methods=['GET', 'POST'])
def createcountry():
    form = CreateCountry()
    if form.validate_on_submit():
        country= Country(name=form.name.data)
        db.session.add(country)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create_country.html', form=form)

@app.route('/updateuser/<int:id>', methods=['GET', 'POST'])
def updateuser(id):
    form = CreateUser()
    user = User.query.filter_by(id=id).first()

    if form.validate_on_submit():
        user.name = form.name.data
        user.age = form.age.data
        user.gender = form.gender.data
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('update_user.html', form=form)

@app.route('/updatecountry/<int:id>', methods=['GET', 'POST'])
def updatecountry(id):
    form = CreateCountry()
    country = Country.query.filter_by(id=id).first()

    if form.validate_on_submit():
        country.name = form.name.data
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('update_country.html', form=form)

@app.route('/deletecountry/<int:id>', methods=['GET', 'POST'])
def deletecountry(id):
        join_country = CountryVisit.query.filter_by(country_id=id).all()
        country = Country.query.filter_by(id=id).first()
        for item in join_country:
            db.session.delete(item)         
        db.session.delete(country)
        db.session.commit()
        return redirect(url_for('read'))

@app.route('/deleteuser/<int:id>', methods=['GET', 'POST'])
def deleteuser(id):
        join_country = CountryVisit.query.filter_by(user_id=id).all()
        user = User.query.filter_by(id=id).first()
        for item in join_country:
            db.session.delete(item)         
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('read'))

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    host = os.getenv('HOSTNAME')
    users = User.query.all()
    countrys= Country.query.all()
    country_visit= CountryVisit.query.all()
    user_dict= {}
    for user in users:
        visits = CountryVisit.query.filter_by(user_id=user.id).all()
        country_names = []
        for visit in visits:
            country_names.append(Country.query.get(visit.country_id).name)
        user_dict[user.name] = country_names
    country_dict= {}
    for country in countrys:
        visits = CountryVisit.query.filter_by(country_id=country.id).all()
        user_name = []
        for visit in visits:
            user_name.append(User.query.get(visit.user_id).name)
        country_dict[country.name] = user_name
        
    return render_template('read.html', users=users, countrys=countrys, country_visit=country_visit, user_dict=user_dict, country_dict=country_dict, host=host)

@app.route('/add', methods=['GET', 'POST'])
def connect():
    connect = Add()
    users = User.query.all()
    countrys = Country.query.all()
    for user in users:
        connect.user_name.choices.append(
            (user.id, f"{user.name}"))

    for country in countrys:
        connect.user_country.choices.append(
            (country.id, f"{country.name}"))
    
    if connect.validate_on_submit():
        add = CountryVisit(user_id=connect.user_name.data, country_id=connect.user_country.data)
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('connect.html', form=connect, user=users, country=countrys)
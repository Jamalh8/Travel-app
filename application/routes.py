from application import app, db
from application.models import User, Country, CountryVisit
from application.forms import CreateCountry, CreateUser, Add
from flask import render_template, redirect, url_for, request

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
def deletecountry(id):
        join_country = CountryVisit.query.filter_by(user_id=id).all()
        user = User.query.filter_by(id=id).first()
        for item in join_country:
            db.session.delete(item)         
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('read'))
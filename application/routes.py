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



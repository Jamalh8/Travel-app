from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from application.models import Country, User, CountryVisit

class CreateUser(FlaskForm):
    name = StringField('Name :', validators=[DataRequired()])
    age = IntegerField('Age :', validators=[DataRequired()])
    gender = SelectField('Gender :', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        name_object = User.query.filter_by(name=name.data).first()
        if name_object:
            raise ValidationError ("This user name's already taken, please pick another name.")


class CreateCountry(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        name_object = Country.query.filter_by(name=name.data).first()
        if name_object:
            raise ValidationError ("This country name already exists.")

class Add(FlaskForm):
    user_name= SelectField ("Traveler :", choices=[],validators=[DataRequired()])
    user_country= SelectField ("Country :", choices=[],validators=[DataRequired()])
    submit = SubmitField('Add!')

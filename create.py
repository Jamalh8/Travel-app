from application import db
from application.models import User, Country, CountryVisit

db.drop_all()
db.create_all()
#For current stage keeping drop all function up.
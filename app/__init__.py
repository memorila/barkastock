from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#credentials for logging in a user
from flask_login import LoginManager


app = Flask(__name__)
# used when invoking configurations for flask-wtf, et al
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#credentials for logging in a user
login = LoginManager(app)
login.login_view = 'login'



from app import routes, models


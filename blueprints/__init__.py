from app import app
from flask import render_template
from blueprints.users.views import users_blueprint
from blueprints.sessions.views import sessions_blueprint
from blueprints.home.views import home_blueprint
from models.user import User
from flask_login import LoginManager


app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(sessions_blueprint, url_prefix='/sessions')
app.register_blueprint(home_blueprint, url_prefix='/home')

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(id=user_id)

@app.route('/')
def index():
    return render_template('index.html')

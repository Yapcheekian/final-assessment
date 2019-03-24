from app import app
from flask import render_template
from blueprints.users.views import users_blueprint
from blueprints.sessions.views import sessions_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(sessions_blueprint, url_prefix='/sessions')

@app.route('/')
def index():
    return render_template('index.html')

from flask import Blueprint, render_template

users_blueprint = Blueprint('users', __name__, template_folder='templates/users/')

@users_blueprint.route('/')
def new():
    return render_template('registration.html')


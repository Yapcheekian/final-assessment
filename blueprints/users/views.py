from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User


users_blueprint = Blueprint('users', __name__, template_folder='templates/users/')

@users_blueprint.route('/')
def new():
    return render_template('registration.html')

@users_blueprint.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password)

    user = User(name=name, email=email, password=hashed_password)
    user.save()    

    return redirect(url_for('home.show'))



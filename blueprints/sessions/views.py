from flask import Blueprint, render_template, url_for, redirect, request
from werkzeug.security import check_password_hash
from models.user import User
from flask_login import login_required, login_user, logout_user, current_user

sessions_blueprint = Blueprint('sessions', __name__, template_folder='templates/sessions/')

@sessions_blueprint.route('/')
def login():
    return render_template('login.html')

@sessions_blueprint.route('/check', methods=['POST'])
def check():
    email = request.form['email']
    password = request.form['password']
    user = User.get_or_none(User.email == email)
    hashed_password = user.password
    check_password = check_password_hash(hashed_password, password)

    if check_password:
        login_user(user)
        return redirect(url_for('home.show'))

@sessions_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('sessions.login'))


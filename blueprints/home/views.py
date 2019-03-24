from flask import Blueprint, render_template, url_for
from flask_login import login_required

home_blueprint = Blueprint('home', __name__, template_folder='templates/home/')


@home_blueprint.route('/')
@login_required
def show():
    return render_template('landing.html')

@home_blueprint.route('/new', methods=['POST'])
def create():
    item = request.form['item']
    return 'success'

from flask import Blueprint, render_template

sessions_blueprint = Blueprint('sessions', __name__, template_folder='templates/sessions/')
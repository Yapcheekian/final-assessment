import os
from flask import Flask, render_template, request, url_for
from database import db


app = Flask(__name__)

import blueprints


app.secret_key = os.environ.get('SECRET_KEY')

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response


if __name__ == 'main':
    app.run(debug=True)
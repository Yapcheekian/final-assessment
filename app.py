from flask import Flask, render_template, request, url_for
from models import db


app = Flask(__name__)

import blueprints


@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response


@app.route('/new', methods=['POST'])
def create():
    item = request.form['item']
    return item

@app.route('/landing')
def show():
    return render_template('landing.html')

if __name__ == 'main':
    app.run(debug=True)
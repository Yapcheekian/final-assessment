import os
from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from util.upload import upload_file_to_s3
from models.todo import Todo
from werkzeug.utils import secure_filename

home_blueprint = Blueprint('home', __name__, template_folder='templates/home/')


@home_blueprint.route('/')
@login_required
def show():
    user = current_user.name
    images = current_user.images
    return render_template('landing.html', user=user, images=images)


@home_blueprint.route('/upload/', methods=['POST'])
def upload_file():

    item = request.form['item']
    
	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file    = request.files["user_file"]

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    # if file and allowed_file(file.filename):
    file.filename = secure_filename(file.filename)
    output   	  = upload_file_to_s3(file, os.environ.get("S3_BUCKET"))


    url = Todo(imageUrl=output, text=item, user_id=current_user.id)
    url.save()

    return redirect(url_for('home.show'))

@home_blueprint.route('/complete', methods=['POST'])
def complete():

    imageId = request.form['imageId']

    image = Todo.get_or_none(id=imageId)
    image.is_completed = True
    image.save()

    return redirect(url_for('home.show'))


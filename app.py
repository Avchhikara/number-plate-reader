from os import path, curdir, getenv, makedirs, urandom, remove
from flask import Flask, redirect, request, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
# from flask.ext.session import Session

from utils.checkAllowed import allowed_file


UPLOAD_FOLDER = path.join(path.abspath(curdir), "uploads")
# creating upload folder directory if not exists
makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, static_folder='uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# sess = Session(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'POST' == request.method:
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No attribute with the name file"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return "No filename"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))

            # Do some processing here

            # deleting the file after some processing
            remove(path.join(app.config['UPLOAD_FOLDER'], filename))
            return uploaded_image_view(filename)

    # Otherwise returning the uploader page
    return render_template('index.html')


@app.route('/reading/<path:filename>', methods=["GET", "POST"])
def uploaded_image_view(filename):
    # return send_from_directory(app.config[UPLOAD_FOLDER], filename=filename, as_attachment=True)
    # Sending the file name (except the exception) back as number for now.
    return {
        'registrationNumber': filename.split(".")[0]
    }


if __name__ == "__main__":
    # app.secret_key = urandom(34)
    app.run(debug=True, port=(getenv('PORT') or 1234))

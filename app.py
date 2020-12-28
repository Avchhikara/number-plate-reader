from os import path, curdir, getenv, makedirs
from flask import Flask, redirect, request, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

from utils.checkAllowed import allowed_file


UPLOAD_FOLDER = path.join(path.abspath(curdir), "uploads")
# creating upload folder directory if not exists
makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, static_folder='uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return 'Homepage'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'POST' == request.method:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_image_view',
                                    filename=filename))

    # Otherwise returning the uploader page
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<path:filename>')
def uploaded_image_view(filename):
    return send_from_directory(app.config[UPLOAD_FOLDER], filename=filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=(getenv('PORT') or 1234))

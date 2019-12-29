import os
import io
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, json, jsonify
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import hexadoku

UPLOAD_FOLDER = os.getcwd() + '\\uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # limit file size to 16 MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file(): # process hexadoku
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if file.filename.rsplit('.',1)[1].lower() == "txt":
                # with open("boards\\" + file.filename, "r") as f:
                #     content = f.read()
                # content = hexadoku.solve(content)
                file_path = "boards\\" + file.filename
                content = hexadoku.solve(file_path)
                
                return redirect(url_for('uploaded_file', filename=content, file_type="text"))
                
            else:
                mem_file = io.BytesIO()
                file.save(mem_file)
                data = np.fromstring(mem_file.getvalue(), dtype=np.uint8)
                img = cv2.imdecode(data, -1)

                output_img = hexadoku.read_board(img)
                cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], filename),output_img)

                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file', filename=filename, file_type="image"))
    return render_template('home.html')

@app.route('/solution/<file_type>/<filename>')
def uploaded_file(filename, file_type):
    if(file_type == "image"):
        filename = 'http://localhost:5000/uploads/' + filename
        return render_template('template.html', filename=filename)
    elif(file_type == "text"):
        return render_template('solution_txt.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()
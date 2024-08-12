from flask import Flask, render_template, request, Response, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sys

sys.path.insert(0, 'C:/Users/sharm/Downloads/ISRO/Models/Super_Resolution/SRGAN')

import generate_srgan

#from db import db_init, db
#from models import Img

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/sharm/Downloads/ISRO/Models/Super_Resolution/SRGAN/generate_data/TMC2/singletest_1x'
OUTPUT_4x_FOLDER = 'C:/Users/sharm/Downloads/ISRO/Models/Super_Resolution/SRGAN/generate_data/TMC2/singletest_4x'
OUTPUT_16x_FOLDER = 'C:/Users/sharm/Downloads/ISRO/Models/Super_Resolution/SRGAN/generate_data/TMC2/singletest_16x'
DIM26_FOLDER = 'C:/Users/sharm/Downloads/ISRO/Models/Super_Resolution/SRGAN/generate_data/TMC2/dim24'
DIM96_FOLDER = 'C:/Users/sharm/Downloads/ISRO/Models/Super_Resolution/SRGAN/generate_data/TMC2/dim96'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_4x_FOLDER'] = OUTPUT_4x_FOLDER
app.config['OUTPUT_16x_FOLDER'] = OUTPUT_16x_FOLDER
app.config['DIM26_FOLDER'] = DIM26_FOLDER
app.config['DIM96_FOLDER'] = DIM96_FOLDER

def clean_folder(foldername):
    folder_path = app.config[foldername]
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path):  # uncomment if you want to delete subdirectories
            #     shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
            
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pic' not in request.files:
        return 'No file part'

    pic = request.files['pic']

    # If the user does not select a file, the browser submits an empty file without a filename
    if pic.filename == '':
        return 'No selected file'

    clean_folder('UPLOAD_FOLDER')
    
    # Make sure the filename is secure to avoid any potential security issues
    filename = secure_filename(pic.filename)

    # Save the file to the specified upload folder
    pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return redirect(url_for('loading')) 

@app.route('/loading')
def loading():
    clean_folder('DIM26_FOLDER')
    clean_folder('DIM96_FOLDER')
    clean_folder('OUTPUT_4x_FOLDER')
    clean_folder('OUTPUT_16x_FOLDER')
    
    generate_srgan.generate_sr()
        
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run()
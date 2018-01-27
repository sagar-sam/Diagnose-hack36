from flask import Flask, render_template, redirect, url_for, request
from flask_table import Table, Col
from os import listdir
from os.path import isfile, join
import os, os.path
import numpy as np
import pandas as pd
import time, datetime
import subprocess
import pickle
import math
from tkinter.filedialog import askopenfilename
from shutil import copyfile
from werkzeug import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dname = os.path.dirname(os.path.abspath(__file__))

@app.route('/teeth',methods=['POST','GET'])
def teeth():
	return render_template("teeth.html")

@app.route('/teethupload',methods=['POST','GET'])
def teethupload():
	if request.method == 'POST':
		myfile = request.files['image']
		f = os.path.join(app.config['UPLOAD_FOLDER']+'/tf_files/', 'teeth.jpeg')
		myfile.save(f)

		subprocess.call("bash predict.sh > result.txt", shell=True)
		filename = "result.txt"

		file = open(filename, "r")

		x = file.readlines()
		y = x[3].split(' ')[0]+' '+x[3].split(' ')[1]
		return render_template("result.html", result=y)

@app.route('/')
def home():
	return render_template('hackapp.html')

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
	app.run(debug = True)
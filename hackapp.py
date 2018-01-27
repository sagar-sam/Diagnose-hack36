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
import predict

app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dname = os.path.dirname(os.path.abspath(__file__))

'''
def open_file():
	global file_name
	file_name = askopenfilename(filetypes= (("ALL files","*.*"),("Image files","*jpg")))    
	return file_name

@app.route('/openfile',methods = ['POST','GET'])
def openfile():
	if request.method == 'POST':
		return render_template("check.html",check=open_file())
'''

@app.route('/upload',methods=['POST','GET'])
def upload():
	if request.method == 'POST':
		myfile = request.files['image']
		f = os.path.join(app.config['UPLOAD_FOLDER']+'/tf_files/', 'fuckall.jpeg')
		myfile.save(f)
		subprocess.call("bash predict.sh", shell=True)
		return render_template("hackapp.html")

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
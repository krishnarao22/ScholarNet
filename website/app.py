'''
This is the main file containing the backend code that serves our website
'''

import sys

# sys.path.append('/Users/krishnarao/opt/anaconda3/envs/ScholarNet/bin/')
from flask import Flask, render_template, request
from src.resumeParser import hello, parseResume
from src.opportunityCreator import createOpportunity
from src.login import login

app = Flask(__name__)

@app.route('/')
def landing():
    print(sys.path)
    return render_template('landing.html')

@app.route('/upload', methods=['GET'])
def upload_get():
    return render_template('upload.html')

# on the POST request, accept the file upload
# after the file is uploaded, a function should be called to process the file
@app.route('/upload', methods=['POST'])
def upload_post():
    # get the file from the request
    file = request.files['file']
    # process the file
    return parseResume(file)

@app.route('/opportunity_create', methods=['GET'])
def opportunity_create_get():
    return render_template('opportunity_create.html')

@app.route('/opportunity_create', methods=['POST'])
def opportunity_create_post():
    return createOpportunity()

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    return login()

if __name__ == '__main__':
    app.run(debug=True)
'''
This is the main file containing the backend code that serves our website
'''

import sys
import msal

# sys.path.append('/Users/krishnarao/opt/anaconda3/envs/ScholarNet/bin/')
from flask import Flask, render_template, request
from src.resumeParser import hello, parseResume
from src.opportunityCreator import createOpportunity
from src.login import login
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

# database stuff
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'

# Initialize MySQL
mysql = MySQL(app)

def create_database():
    cur = mysql.connection.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS your_database_name')
    cur.close()

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
    form = OpportunityForm(request.form)

    if form.validate():
        result = createOpportunity(
            name=form.name.data,
            age=form.age.data,
            description=form.description.data,
            keywords=form.keywords.data
        )

        return redirect(url_for('success_page'))
    else:
        return render_template('opportunity_create.html', form=form)

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def def_login_post():
    return default_login()


@app.route('/microsoft_login', methods=['GET'])
def login_post():
    return login()

if __name__ == '__main__':
    app.run(debug=True)
import sys
# sys.path.append('/Users/krishnarao/opt/anaconda3/envs/ScholarNet/bin/')
from flask import Flask, render_template, request
from src.resumeParser import hello, parseResume
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

if __name__ == '__main__':
    app.run(debug=True)
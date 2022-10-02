from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))


@app.route('/amiok/<fullPatientInfos>')
def display(fullPatientInfos):
    patientInfos = escape(fullPatientInfos).split(':')
    return render_template('index.html', fullInfos=escape(fullPatientInfos),
                           patientName=patientInfos[0], doctorName=patientInfos[1],
                           Symptomes=patientInfos[2], Diagnosis=patientInfos[3],
                           Prescription=patientInfos[4])

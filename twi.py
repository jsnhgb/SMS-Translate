from flask import Flask
from flask import request
from flask import url_for, redirect
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix
from twilio import twiml
from twilio.rest import TwilioRestClient
import os
from random import randint

# Declare and configure application
app = Flask(__name__)
app.config['ACCOUNT_SID'] = 'ACe00bbbd006337d3d53e3c84d0525dd46'
app.config['AUTH_TOKEN'] = '0fab38df4e6f2b6321fcdc91774bacf6'
app.config['SONYA_APP_SID'] ='APdc1d4351cd866dedeb09ece15f2e8cb0'
# app.config['SONYA_CALLER_ID'] = SONYA_CALLER_ID


@app.route('/')
def index():
    question = ("hello twi")
    return str(question)

@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    client = TwilioRestClient(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])
    r = client.sms.messages.create(to=request.form['From'], from_="+19177461980", body = request.form['Body'])
    return str(r)


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()


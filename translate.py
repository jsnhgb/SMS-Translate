from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix
from twilio import twiml
from twilio.rest import TwilioRestClient
from apiclient.discovery import build


# Declare and configure application
app = Flask(__name__)
app.config['ACCOUNT_SID'] = 'ACe00bbbd006337d3d53e3c84d0525dd46'
app.config['AUTH_TOKEN'] = '0fab38df4e6f2b6321fcdc91774bacf6'
app.config['TRANSLATE_KEY'] = 'AIzaSyCtwxiJRg35WTPdhLApleT6RKipMn78kqE'
#app.config['SONYA_APP_SID'] = 'APdc1d4351cd866dedeb09ece15f2e8cb0'
# app.config['SONYA_CALLER_ID'] = SONYA_CALLER_ID


@app.route('/')
def index():
    question = ("hello twi")
    return str(question)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    client = TwilioRestClient(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])
    service = build('translate', 'v2', developerKey=app.config['TRANSLATE_KEY'])
    body = request.form['Body']
#    if body.find('*') == '#':
#        lang = body[1:2]
#        query = body[4:]
#    else:
#        lang = 'fr'
#        query = body
    gtrans = service.translations().list(target='fr', format='text', q=body).execute()
    if gtrans['translations'][0]['detectedSourceLanguage'] != 'en':
        #if lang not english then translate that into english
        gtrans = service.translations().list(target='en', format='text', q=body).execute()
    r = client.sms.messages.create(to=request.form['From'], from_="+19177461980",
                                   body=gtrans['translations'][0]['translatedText'])
    return str(r)


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()

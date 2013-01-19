from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix
from twilio import twiml
from twilio.rest import TwilioRestClient
from apiclient.discovery import build
from unidecode import unidecode

# Declare and configure application
app = Flask(__name__)
app.config['ACCOUNT_SID'] = 'key goes here'
app.config['AUTH_TOKEN'] = 'key goes here'
app.config['TRANSLATE_KEY'] = 'key goes here'


@app.route('/')
def index():
    '''index path to make sure Flask app is up and running.'''
    question = ("hello twi")
    return str(question)


@app.route('/sms', methods=['POST'])
def sms():
    '''Translate from english to french and vice versa'''
    r = twiml.Response()
    client = TwilioRestClient(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])
    service = build('translate', 'v2', developerKey=app.config['TRANSLATE_KEY'])
    body = request.form['Body']
    gtrans = service.translations().list(target='fr', format='text', q=body).execute()
    if gtrans['translations'][0]['detectedSourceLanguage'] != 'en':
        #if lang not english then translate that into english
        gtrans = service.translations().list(target='en', format='text', q=body).execute()
    r = client.sms.messages.create(to=request.form['From'], from_="+19177461980",
                                   body=unidecode(gtrans['translations'][0]['translatedText']))
    return str(r)


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()

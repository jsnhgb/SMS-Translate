#
# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Translate.

Command-line application that translates some text.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from apiclient.discovery import build
import json
#import HTMLParser


def main():

    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('translate', 'v2', developerKey='AIzaSyCtwxiJRg35WTPdhLApleT6RKipMn78kqE')
    #h = HTMLParser.HTMLParser()
    french = service.translations().list(target='fr', format='text',
                                         q=['flower it \
                                            is cold outside because it is winter']
                                         ).execute()
    print type(french)
    #pretty = h.unescape(french)
    tt = json.dumps(french, ensure_ascii=False)
    print type(tt)
    print tt
    td = json.loads(tt)
    print type(td)
    print td['translations'][0]['translatedText']

if __name__ == '__main__':
    main()

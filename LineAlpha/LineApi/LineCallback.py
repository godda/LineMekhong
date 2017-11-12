# -*- coding: utf-8 -*-
import requests
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Enter PinCode '" + pin + "' to your mobile phone in 2 minutes")

    def QrUrl(self, url):
        self.callback("Login qrcode to your smartphone in 2 minutes\n" + url)

        ACCESS_TOKEN = 'c4Pw8CiaQj7LWo4qLcigrsJc2v2pRLsItUK8SX4rSWC'
        MESSAGE =  '>>> ' + url

        URL = 'https://notify-api.line.me/api/notify'
        MESSAGE_FIELD = {'message' : MESSAGE}

        LINE_HEADERS = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
        }
        try:
            response = requests.post(
            url=URL,
            headers=LINE_HEADERS,
            data=MESSAGE_FIELD
            )
            print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
        
    def default(self, str):
        self.callback(str)

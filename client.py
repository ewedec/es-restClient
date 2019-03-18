import yaml
import logging
import sys
import requests


class Client(object):

    def __init__(self, url, header=None, params=None):
        self.url = url
        self.header = header
        self.params = params

    def get(self):
        response = requests.get(url=self.url, headers=self.header, params=self.params)
        status = response.status_code
        if status == 200:
            return response.text
        else:
            return response.status_code

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

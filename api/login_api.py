import requests

from app import ihrm_url


class LoginApi:
    def __init__(self):
        self.login_url = ihrm_url+"/api/sys/login"

    def login(self, jsonData, headers):
        return requests.post(url=self.login_url,
                             json=jsonData,
                             headers=headers)

from core_lib.APICoreLib import APICoreLib
import json
import urllib.parse

class ApiModel:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api = APICoreLib()
        self.access_token = ""

    def build_url(self, endpoint):
        return urllib.parse(self.base_url, endpoint)

    def send_request(self, method, endpoint, **kwargs):
        url = self.build_url(endpoint)
        return self.api.send_request(method, url, **kwargs)

    def get_access_token(self, payload):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        resp = self.send_request(method="POST", endpoint="/auth/login", headers=headers, data=json.dumps(payload))
        self.access_token = resp.get("body").get("accessToken")
        return resp

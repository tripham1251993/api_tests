from pom.api.ApiModel import ApiModel


class UserAPI(ApiModel):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_me(self):
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
        }
        payload = {}
        endpoint = "/api/users/me"
        return self.send_request("get", endpoint, headers=headers, data=payload)

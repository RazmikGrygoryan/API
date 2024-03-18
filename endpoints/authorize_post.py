import allure
import requests

from endpoints.endpoint import EndPoint


class CreateAuthToken(EndPoint):
    auth_token = None

    @allure.step('Create new auth token')
    def create_new_auth_token(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/authorize', json=payload, headers=headers)
        self.json = self.response.json()
        self.auth_token = self.json['token']
        return self.response

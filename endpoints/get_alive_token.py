import allure
import requests

from endpoints.endpoint import EndPoint


class GetAliveToken(EndPoint):
    @allure.step('Check that auth token is alive')
    def get_alive_auth_token(self, auth_token, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/authorize/{auth_token}', headers=headers)
        return self.response

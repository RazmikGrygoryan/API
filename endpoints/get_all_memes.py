import allure
import requests

from endpoints.endpoint import EndPoint


class GetAllMemes(EndPoint):
    @allure.step('Check all memes')
    def get_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        self.json = self.response.json()
        return self.response

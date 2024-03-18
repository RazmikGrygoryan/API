import allure
import requests

from endpoints.endpoint import EndPoint


class CreateMeme(EndPoint):
    meme_id = None

    @allure.step('Create new meme')
    def create_new_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=payload, headers=headers)
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response

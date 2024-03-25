import allure
import requests

import requests
import allure
from endpoints.endpoint import EndPoint


class CreateMeme(EndPoint):
    meme_id = None
    text = None

    @allure.step('Create new meme')
    def create_new_meme(self, payload, return_text=False, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=payload, headers=headers)
        if return_text:
            self.text = self.response.text
        else:
            self.json = self.response.json()
            self.meme_id = self.json['id']
        return self.response

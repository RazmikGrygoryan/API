import allure
import requests

from endpoints.endpoint import EndPoint


class UpdateMeme(EndPoint):
    meme_id = None
    text = None

    @allure.step('Update meme')
    def update_meme(self, meme_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=payload, headers=headers)
        self.json = self.response.json()
        self.text = self.json['text']
        return self.response

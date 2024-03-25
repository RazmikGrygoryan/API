import allure
import requests

from endpoints.endpoint import EndPoint


class UpdateMeme(EndPoint):
    meme_id = None
    text = None

    @allure.step('Update meme')
    def update_meme(self, meme_id, payload, return_text=False, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=payload, headers=headers)
        if return_text:
            self.text = self.response.text
            return self.text
        else:
            self.json = self.response.json()
            self.text = self.json['text']
            return self.json

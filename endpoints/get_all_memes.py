import allure
import requests

from endpoints.endpoint import EndPoint


class GetAllMemes(EndPoint):
    text = None

    @allure.step('Check all memes')
    def get_all_memes(self, return_text=False, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        if return_text:
            self.text = self.response.text
            return self.text
        else:
            self.json = self.response.json()
            return self.json

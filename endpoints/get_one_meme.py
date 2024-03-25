import allure
import requests

from endpoints.endpoint import EndPoint


class GetOneMemes(EndPoint):
    @allure.step('Get one meme')
    def get_one_memes(self, meme_id, return_text=False, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        if return_text:
            return self.response.text
        else:
            return self.response.json()

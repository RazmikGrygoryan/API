import allure
import requests

from endpoints.endpoint import EndPoint


class GetOneMemes(EndPoint):
    @allure.step('Check all memes')
    def get_one_memes(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        # self.json = self.response.json()
        return self.response

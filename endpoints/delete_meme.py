import allure
import requests

from endpoints.endpoint import EndPoint


class DeleteMeme(EndPoint):
    @allure.step('Delete Meme')
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)
        return self.response

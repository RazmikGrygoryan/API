import allure


class EndPoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that page NOT FOUND')
    def check_bad_request(self):
        assert self.response.status_code == 404

    @allure.step('Check that text is the same as sent')
    def check_response_text_is_correct(self, text):
        assert self.json['text'] == text

    @allure.step('Check that data in response')
    def check_data_in_response(self):
        assert 'data' in self.json

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
    def check_page_not_found(self):
        assert self.response.status_code == 404

    @allure.step('Check that 401 Unauthorized')
    def check_is_unathorized(self):
        assert self.response.status_code == 401

    @allure.step('400 Bad Request')
    def check_bad_request(self):
        assert self.response.status_code == 400

    @allure.step('Check that text is the same as sent')
    def check_response_is_correct(self, text, info, tags, url):
        assert self.json['text'] == text
        assert self.json['info'] == info
        assert self.json['tags'] == tags
        assert self.json['url'] == url

    @allure.step('Check that data in response')
    def check_data_in_response(self):
        assert 'data' in self.json and isinstance(self.json['data'], list)

        for item in self.json['data']:
            assert 'id' in item and 'info' in item and 'tags' in item

    @allure.step('Check invalid data in error')
    def check_invalid_data(self, text):
        assert "Invalid parameters" in text

    @allure.step('Check that 403 Forbidden')
    def check_is_forbidden(self):
        assert self.response.status_code == 403

    @allure.step('Check id is correct')
    def check_is_id(self, id):
        assert self.json['id'] == id

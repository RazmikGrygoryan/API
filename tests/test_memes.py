import pytest


def test_all_memes(get_all_memes, auth_token):
    get_all_memes.get_all_memes(headers={"Authorization": auth_token})
    get_all_memes.check_that_status_is_200()
    get_all_memes.check_data_in_response()


def test_post_meme(create_meme, auth_token):
    payload = {
        "text": "Meme",
        "url": "Meme",
        "tags": ["Meme"],
        "info": {"Meme": 777}
    }
    create_meme.create_new_meme(payload, headers={"Authorization": auth_token})
    create_meme.check_that_status_is_200()
    create_meme.check_response_is_correct(payload['text'], payload['info'], payload['tags'], payload['url'])


def test_one_meme(get_meme, auth_token, meme_id):
    get_meme.get_one_memes(meme_id, headers={"Authorization": auth_token})
    get_meme.check_that_status_is_200()
    get_meme.check_is_id(meme_id)


def test_update_meme(update_meme, auth_token, meme_id):
    payload = {
        "id": meme_id,
        "text": "Meme111",
        "url": "Mem",
        "tags": ["Meme111"],
        "info": {"Meme": 77777}
    }
    update_meme.update_meme(meme_id, payload, headers={"Authorization": auth_token})
    update_meme.check_that_status_is_200()
    update_meme.check_response_is_correct(payload['text'], payload['info'], payload['tags'], payload['url'])


def test_delete_meme(delete_meme, get_meme, auth_token, meme_id):
    delete_meme.delete_meme(meme_id, headers={"Authorization": auth_token})
    get_meme.get_one_memes(meme_id, True, headers={"Authorization": auth_token})
    delete_meme.check_that_status_is_200()
    get_meme.check_page_not_found()


@pytest.mark.parametrize("invalid_payload", [
    {1: 1},
    {2: 1},
    {3: "  "},
    {4: True}
])
def test_failed_data_post(create_meme, auth_token, invalid_payload):
    create_meme.create_new_meme(invalid_payload, True, headers={"Authorization": auth_token})
    create_meme.check_bad_request()


def test_with_incorrect_token(get_all_memes):
    get_all_memes.get_all_memes(True, headers={"Authorization": "123"})
    get_all_memes.check_is_unathorized()


def test_get_all_memes_without_token(get_all_memes):
    get_all_memes.get_all_memes(True)
    get_all_memes.check_is_unathorized()


def test_post_meme_without_token(create_meme):
    create_meme.create_new_meme(True)
    create_meme.check_is_unathorized()


def test_update_meme_without_token(update_meme):
    update_meme.update_meme(True)
    update_meme.check_is_unathorized()


def test_without_data(update_meme, auth_token, meme_id):
    payload = {
        "id": meme_id,
    }
    update_meme.update_meme(meme_id, payload, True, headers={"Authorization": auth_token})
    update_meme.check_bad_request()
    update_meme.check_invalid_data(update_meme.text)


def test_update_stranger_meme(get_all_memes, update_meme, auth_token):
    get_all_memes.get_all_memes(headers={"Authorization": auth_token})
    for meme in get_all_memes.json.get('data', []):
        if 'updated_by' in meme and meme.get('updated_by') != 'Razmik':
            payload = {
                "id": meme['id'],
                "text": "Meme111",
                "url": "Mem",
                "tags": ["Meme111"],
                "info": {"Meme": 77777}
            }
            update_meme.update_meme(meme['id'], payload, True, headers={"Authorization": auth_token})
            update_meme.check_is_forbidden()
            break


def test_delete_stranger_meme(get_all_memes, delete_meme, auth_token):
    get_all_memes.get_all_memes(headers={"Authorization": auth_token})
    for meme in get_all_memes.json.get('data', []):
        if 'updated_by' in meme and meme.get('updated_by') != 'Razmik':
            delete_meme.delete_meme(meme['id'], headers={"Authorization": auth_token})
            delete_meme.check_is_forbidden()
            break


def test_delete_unexisted_meme(delete_meme, auth_token):
    delete_meme.delete_meme('ddd', headers={"Authorization": auth_token})
    delete_meme.check_page_not_found()


def test_update_unexisted_meme(update_meme, auth_token):
    payload = {
        "id": 'ddd',
        "text": "Meme111",
        "url": "Meme",
        "tags": ["Meme111"],
        "info": {"Meme": 77777}
    }
    update_meme.update_meme('ddd', payload, True, headers={"Authorization": auth_token})
    update_meme.check_page_not_found()

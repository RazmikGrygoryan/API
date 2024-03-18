import pytest
import random


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
    create_meme.check_response_text_is_correct(payload['text'])


def test_one_meme(get_meme, auth_token, meme_id):
    get_meme.get_one_memes(meme_id, headers={"Authorization": auth_token})
    get_meme.check_that_status_is_200()


def test_update_meme(update_meme, auth_token, meme_id):
    payload = {
        "id": meme_id,
        "text": "Meme111",
        "url": "Meme111",
        "tags": ["Meme111"],
        "info": {"Meme": 77777}
    }
    update_meme.update_meme(meme_id, payload, headers={"Authorization": auth_token})
    update_meme.check_that_status_is_200()
    update_meme.check_response_text_is_correct(payload['text'])


def test_delete_meme(delete_meme, get_meme, auth_token, meme_id):
    delete_meme.delete_meme(meme_id, headers={"Authorization": auth_token})
    get_meme.get_one_memes(meme_id, headers={"Authorization": auth_token})
    delete_meme.check_that_status_is_200()
    get_meme.check_bad_request()

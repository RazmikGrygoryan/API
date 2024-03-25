import pytest

from endpoints.authorize_post import CreateAuthToken
from endpoints.get_alive_token import GetAliveToken
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_meme import GetOneMemes
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def get_all_memes():
    return GetAllMemes()


@pytest.fixture()
def get_meme():
    return GetOneMemes()


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture(scope="session")
def auth_token(create_auth_token):
    payload = {"name": "Razmik"}
    create_auth_token.create_new_auth_token(payload)
    return create_auth_token.auth_token


@pytest.fixture(scope="session", autouse=True)
def check_token_is_alive(get_token, create_auth_token, auth_token):
    if "Token is alive." in get_token.get_alive_auth_token(auth_token):
        pass
    else:
        payload = {"name": "Razmik"}
        create_auth_token.create_new_auth_token(payload)
        return create_auth_token.auth_token


@pytest.fixture()
def meme_id(create_meme, auth_token):
    payload = {
        "text": "ddd",
        "url": "eee",
        "tags": [121123, 12],
        "info": {"1": 2}
    }
    create_meme.create_new_meme(payload, headers={"Authorization": auth_token})
    yield create_meme.meme_id


@pytest.fixture(scope="session")
def get_token():
    return GetAliveToken()


@pytest.fixture(scope="session")
def create_auth_token():
    return CreateAuthToken()

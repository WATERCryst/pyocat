import httpx

from configparser import RawConfigParser
from pyocat import Auth, ApiClient


def load_key():
    config = RawConfigParser()
    config.read(r'keys.toml')
    key = config['keys']['key']
    return key.strip('"')


key = load_key()


def test_get_state():
    with httpx.Client() as client:
        auth = Auth(client, key)
        api = ApiClient(auth)
        state = api.get_state()
        assert False, repr(state)

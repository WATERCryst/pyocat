from configparser import RawConfigParser

from pyocat import BiocatRestApiClient


def load_key():
    config = RawConfigParser()
    config.read(r'keys.toml')
    key = config['keys']['key']
    return key.strip('"')


key = load_key()


def test_get_state():
    with BiocatRestApiClient(key) as client:
        state = client.get_state()
        assert False, repr(state)

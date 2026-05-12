import pytest
import httpx

from configparser import RawConfigParser
from pyocat import AsyncAuth, AsyncApiClient


def load_key():
    config = RawConfigParser()
    config.read(r'keys.toml')
    key = config['keys']['key']
    return key.strip('"')


key = load_key()


@pytest.mark.asyncio
async def test_get_state():
    async with httpx.AsyncClient() as client:
        auth = AsyncAuth(client, key)
        api = AsyncApiClient(auth)
        state = await api.get_state()
        assert False, repr(state)

from typing import Any

import httpx

from datetime import datetime
from configparser import RawConfigParser
from pydantic_core import TzInfo
from pyocat import Auth, ApiClient


def load_key():
    config = RawConfigParser()
    config.read(r'keys.toml')
    key = config['keys']['key']
    return key.strip('"')


key = load_key()


def test_get_measurements(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/measurements/direct'
    JSON: dict[str, Any] = {
        "waterTemp": 24,
        "pressure": 3.88,
        "flowRate": 4.5,
        "lastWaterTapVolume": 15.3,
        "lastWaterTapDuration": 30.1,
    }
    httpx_mock.add_response(url=URL, json=JSON) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, key)
        api = ApiClient(auth)
        resp = api.get_measurements()
        assert resp.water_temp == 24
        assert resp.pressure == 3.88
        assert resp.flow_rate == 4.5
        assert resp.last_water_tap_volume == 15.3
        assert resp.last_water_tap_duration == 30.1


def test_get_state(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/state?locale=de&format=plain'
    JSON: dict[str, Any] = {
        "online": True,
        "mode": {
            "id": "ER",
            "name": "Error"
        },
        "event": {
            "type": "event",
            "eventId": 65,
            "category": "error",
            "title": "65 --  Mindestvolumenstrom unterschritten",
            "description": "Der Mindestvolumenstrom wurde nicht erreicht oder hat die vorgegebene Grenze unterschritten.",
            "timestamp": "2026-05-12T14:54:00Z"
        },
        "waterProtection": {
            "absenceModeEnabled": True,
            "pauseLeakageProtectionUntilUTC": "2000-01-01T00:00:00Z"
        },
        "mlState": "running",
    }
    httpx_mock.add_response(url=URL, json=JSON) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, key)
        api = ApiClient(auth)
        resp = api.get_state()
        assert resp.online == True
        assert resp.mode.id == "ER"
        # TODO: alles abtesten.


# https://pypi.org/project/pytest-httpx/
# https://dev.to/bowmanjd/getting-started-with-httpx-part-2-pytest-and-pytesthttpx-2jef
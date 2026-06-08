from typing import Any

import httpx

from datetime import datetime
from pydantic_core import TzInfo
from pyocat import Auth, ApiClient


def test_acknowledge_event(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/ackevent'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.acknowledge_event()


def test_enable_absence(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/absence/enable'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.enable_absence()


def test_disable_absence(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/absence/disable'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.disable_absence()


def test_pause_leakage_protection(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/leakageprotection/pause?minutes=10'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.pause_leakage_protection(10)


def test_unpause_leakage_protection(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/leakageprotection/unpause'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.unpause_leakage_protection()


def test_start_self_test(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/selftest'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.start_self_test()


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
        auth = Auth(client, "")
        api = ApiClient(auth)
        resp = api.get_measurements()
        assert resp.water_temp == 24
        assert resp.pressure == 3.88
        assert resp.flow_rate == 4.5
        assert resp.last_water_tap_volume == 15.3
        assert resp.last_water_tap_duration == 30.1


def test_start_micro_leakage_measurement(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/mlmeasurement/start'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.start_micro_leakage_measurement()


def test_get_daily_statistics(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/statistics/daily/direct'
    JSON: dict[str, Any] = {
        "type": "statistics",
        "entries": [
            { "consumption": 500.1, "date": "2026-01-01T00:00:00Z" },
            { "consumption": 501.1, "date": "2026-01-02T00:00:00Z" },
            { "consumption": 502.1, "date": "2026-01-03T00:00:00Z" },
        ],
    }
    httpx_mock.add_response(url=URL, json=JSON) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        resp = api.get_daily_statistics()
        assert resp.type == 'statistics'
        assert len(resp.entries) == 3
        assert resp.entries[0].consumption == 500.1
        assert resp.entries[0].date == datetime(2026, 1, 1, tzinfo=TzInfo(0))
        assert resp.entries[1].consumption == 501.1
        assert resp.entries[1].date == datetime(2026, 1, 2, tzinfo=TzInfo(0))
        assert resp.entries[2].consumption == 502.1
        assert resp.entries[2].date == datetime(2026, 1, 3, tzinfo=TzInfo(0))


def test_get_todays_consumption(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/statistics/cumulative/daily'
    JSON = 123.4
    httpx_mock.add_response(url=URL, json=JSON) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        resp = api.get_todays_consumption()
        assert resp == 123.4


def test_get_total_consumption(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/statistics/cumulative/total'
    JSON = 12345678.9
    httpx_mock.add_response(url=URL, json=JSON) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        resp = api.get_total_consumption()
        assert resp == 12345678.9


def test_open_water_supply(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/watersupply/open'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.open_water_supply()


def test_close_water_supply(httpx_mock): # type: ignore
    URL = 'https://appapi.watercryst.com/v1/watersupply/close'
    httpx_mock.add_response(url=URL) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        api.close_water_supply()


def test_get_state_1(httpx_mock): # type: ignore
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
        }
    }
    httpx_mock.add_response(url=URL, json=JSON) # type: ignore
    with httpx.Client() as client:
        auth = Auth(client, "")
        api = ApiClient(auth)
        resp = api.get_state()
        assert resp.online
        assert resp.mode.id == "ER"
        assert resp.mode.name == "Error"
        assert resp.event.type == "event"
        assert resp.event.event_id == 65
        assert resp.event.category == "error"
        assert resp.event.title == "65 --  Mindestvolumenstrom unterschritten"
        assert resp.event.description == "Der Mindestvolumenstrom wurde nicht erreicht oder hat die vorgegebene Grenze unterschritten."
        assert resp.event.timestamp == datetime(2026, 5, 12, 14, 54, tzinfo=TzInfo(0))


def test_get_state_2(httpx_mock): # type: ignore
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
        auth = Auth(client, "")
        api = ApiClient(auth)
        resp = api.get_state()
        assert resp.online
        assert resp.mode.id == "ER"
        assert resp.mode.name == "Error"
        assert resp.event.type == "event"
        assert resp.event.event_id == 65
        assert resp.event.category == "error"
        assert resp.event.title == "65 --  Mindestvolumenstrom unterschritten"
        assert resp.event.description == "Der Mindestvolumenstrom wurde nicht erreicht oder hat die vorgegebene Grenze unterschritten."
        assert resp.event.timestamp == datetime(2026, 5, 12, 14, 54, tzinfo=TzInfo(0))
        if resp.water_protection:
            assert resp.water_protection.absence_mode_enabled
            assert resp.water_protection.pause_leakage_protection_until_utc == datetime(2000, 1, 1, tzinfo=TzInfo(0))
        assert resp.ml_state == "running"

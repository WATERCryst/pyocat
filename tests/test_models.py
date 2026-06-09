from datetime import datetime

from pyocat.models import (
    EventResponse, 
    MeasurementResponse,
    MessageResponse,
    ModeResponse,
    StateResponse,
    StatisticsResponse,
    WaterProtectionResponse
)


def test_event_response_serialization():
    res = EventResponse(
        event_id=0,
        category="info",
        title="Unknown Event",
        description="Unknown Event",
        timestamp=datetime(2026, 6, 8, 13, 13),
    )
    json = '{"eventId":0,"category":"info","title":"Unknown Event","description":"Unknown Event","timestamp":"2026-06-08T13:13:00"}'
    assert res.model_dump_json() == json


def test_event_response_deserialization():
    res = EventResponse(
        event_id=0,
        category="info",
        title="Unknown Event",
        description="Unknown Event",
        timestamp=datetime(2026, 6, 8, 13, 13),
    )
    json = """
    {
        "type": "event",
        "eventId": 0,
        "category": "info",
        "title": "Unknown Event",
        "description": "Unknown Event",
        "timestamp": "2026-06-08T13:13:00"
    }
    """
    assert EventResponse.model_validate_json(json) == res


def test_measurement_response_serialization():
    res = MeasurementResponse(
        water_temp=24,
        pressure=3.2,
        flow_rate=6.4,
        last_water_tap_volume=53.4,
        last_water_tap_duration=234
    )
    json = '{"waterTemp":24,"pressure":3.2,"flowRate":6.4,"lastWaterTapVolume":53.4,"lastWaterTapDuration":234}'
    assert res.model_dump_json() == json


def test_measurement_response_deserialization():
    res = MeasurementResponse(
        water_temp=24,
        pressure=3.2,
        flow_rate=6.4,
        last_water_tap_volume=53.4,
        last_water_tap_duration=234
    )
    json = """
    {
        "waterTemp": 24,
        "pressure": 3.2,
        "flowRate": 6.4,
        "lastWaterTapVolume": 53.4,
        "lastWaterTapDuration": 234
    }
    """
    assert MeasurementResponse.model_validate_json(json) == res


def test_message_response_serialization():
    res = MessageResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 9, 14, 58)
    )
    json = '{"absenceModeEnabled":true,"pauseLeakageProtectionUntilUTC":"2026-06-09T14:58:00"}'
    assert res.model_dump_json() == json


def test_message_response_deserialization():
    pass


def test_mode_response_serialization():
    res = ModeResponse(
        id="TD",
        name="Thermal Disinfection"
    )
    json = '{"id":"TD","name":"Thermal Disinfection"}'
    assert res.model_dump_json() == json


def test_mode_response_deserialization():
    res = ModeResponse(
        id="TD",
        name="Thermal Disinfection"
    )
    json = """
    {
        "id": "TD",
        "name": "Thermal Disinfection"
    }
    """
    assert ModeResponse.model_validate_json(json) == res



from datetime import datetime

from pyocat.models import (
    EventResponse, 
    MeasurementResponse,
    MessageResponse,
    ModeResponse,
    StateResponse,
    StatisticsResponse,
    StatisticsResponseEntry,
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
        "type": "measurement",
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
    res = MessageResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 9, 14, 58)
    )
    json = """
    {
        "absenceModeEnabled": true,
        "pauseLeakageProtectionUntilUTC": "2026-06-09T14:58:00"
    }
    """
    assert MessageResponse.model_validate_json(json) == res


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


def test_state_response_serialize():
    res = StateResponse(
        online=True,
        mode=ModeResponse(
            id="TD",
            name="Thermal Disinfection"
        ),
        event=EventResponse(
            event_id=0,
            category="info",
            title="Unknown Event",
            description="Unknown Event",
            timestamp=datetime(2026, 6, 8, 13, 13),  
        ),
        water_protection=WaterProtectionResponse(
            absence_mode_enabled=True,
            pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16)
        ),
        ml_state='success'
    )
    json = '{"online":true,"mode":{"id":"TD","name":"Thermal Disinfection"},"event":{"eventId":0,"category":"info","title":"Unknown Event","description":"Unknown Event","timestamp":"2026-06-08T13:13:00"},"waterProtection":{"absenceModeEnabled":true,"pauseLeakageProtectionUntilUTC":"2026-06-10T14:16:00"},"mlState":"success"}'
    assert res.model_dump_json() == json


def test_state_response_deserialize():
    res = StateResponse(
        online=True,
        mode=ModeResponse(
            id="TD",
            name="Thermal Disinfection"
        ),
        event=EventResponse(
            event_id=0,
            category="info",
            title="Unknown Event",
            description="Unknown Event",
            timestamp=datetime(2026, 6, 8, 13, 13),  
        ),
        water_protection=WaterProtectionResponse(
            absence_mode_enabled=True,
            pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16)
        ),
        ml_state='success'
    )
    json = """
    {
        "online": true,
        "mode": {
            "id": "TD",
            "name": "Thermal Disinfection"
        },
        "event": {
            "type": "event",
            "eventId": 0,
            "category": "info",
            "title": "Unknown Event",
            "description": "Unknown Event",
            "timestamp": "2026-06-08T13:13:00"
        },
        "waterProtection": {
            "absenceModeEnabled": true,
            "pauseLeakageProtectionUntilUTC": "2026-06-10T14:16:00"
        },
        "mlState": "success"
    }
    """
    assert StateResponse.model_validate_json(json) == res

def test_statistics_response_serialize():
    res = StatisticsResponse(
        entries=[
            StatisticsResponseEntry(
                consumption=123.4,
                date=datetime(2026, 6, 10)
            ),
            StatisticsResponseEntry(
                consumption=234.5,
                date=datetime(2026, 6, 11)
            ),
        ]
    )
    json = '{"entries":[{"consumption":123.4,"date":"2026-06-10T00:00:00"},{"consumption":234.5,"date":"2026-06-11T00:00:00"}]}'
    assert res.model_dump_json() == json


def test_statistics_response_deserialize():
    res = StatisticsResponse(
        entries=[
            StatisticsResponseEntry(
                consumption=123.4,
                date=datetime(2026, 6, 10)
            ),
            StatisticsResponseEntry(
                consumption=234.5,
                date=datetime(2026, 6, 11)
            ),
        ]
    )
    json = """
    {
        "type": "statistics",
        "entries": [
            { "consumption": 123.4, "date": "2026-06-10" },
            { "consumption": 234.5, "date": "2026-06-11" }
        ]
    }
    """
    assert StatisticsResponse.model_validate_json(json) == res

def test_water_protection_response_serialize():
    res = WaterProtectionResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16)
    )
    json = '{"absenceModeEnabled":true,"pauseLeakageProtectionUntilUTC":"2026-06-10T14:16:00"}'
    assert res.model_dump_json() == json


def test_water_protection_response_deserialize():
    res = WaterProtectionResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16)
    )
    json = """
    {
        "absenceModeEnabled": true,
        "pauseLeakageProtectionUntilUTC": "2026-06-10T14:16:00"
    }
    """
    assert WaterProtectionResponse.model_validate_json(json) == res

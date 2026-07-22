from datetime import datetime, UTC

from pyocat.models import (
    DeviceResponse,
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
        timestamp=datetime(2026, 6, 8, 13, 13, tzinfo=UTC),
    )
    json = '{"eventId":0,"category":"info","title":"Unknown Event","description":"Unknown Event","timestamp":"2026-06-08T13:13:00Z"}'
    assert res.model_dump_json() == json


def test_event_response_deserialization():
    res = EventResponse(
        event_id=0,
        category="info",
        title="Unknown Event",
        description="Unknown Event",
        timestamp=datetime(2026, 6, 8, 13, 13, tzinfo=UTC),
    )
    json = """
    {
        "type": "event",
        "eventId": 0,
        "category": "info",
        "title": "Unknown Event",
        "description": "Unknown Event",
        "timestamp": "2026-06-08T13:13:00.0000000Z"
    }
    """
    assert EventResponse.model_validate_json(json) == res


def test_measurement_response_serialization():
    res = MeasurementResponse(
        water_temp=24,
        pressure=3.2,
        flow_rate=6.4,
        todays_consumption=1.23,
        total_consumption=601.56,
        last_water_tap_volume=53.4,
        last_water_tap_duration=234
    )
    json = '{"waterTemp":24,"pressure":3.2,"flowRate":6.4,"todaysConsumption":1.23,"totalConsumption":601.56,"lastWaterTapVolume":53.4,"lastWaterTapDuration":234}'
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
        pause_leakage_protection_until_utc=datetime(2026, 6, 9, 14, 58, tzinfo=UTC)
    )
    json = '{"absenceModeEnabled":true,"pauseLeakageProtectionUntilUTC":"2026-06-09T14:58:00Z"}'
    assert res.model_dump_json() == json


def test_message_response_deserialization():
    res = MessageResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 9, 14, 58, tzinfo=UTC)
    )
    json = """
    {
        "absenceModeEnabled": true,
        "pauseLeakageProtectionUntilUTC": "2026-06-09T14:58:00.0000000Z"
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
            timestamp=datetime(2026, 6, 8, 13, 13, tzinfo=UTC),  
        ),
        water_protection=WaterProtectionResponse(
            absence_mode_enabled=True,
            pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16, tzinfo=UTC)
        ),
        ml_state='success'
    )
    json = '{"online":true,"mode":{"id":"TD","name":"Thermal Disinfection"},"event":{"eventId":0,"category":"info","title":"Unknown Event","description":"Unknown Event","timestamp":"2026-06-08T13:13:00Z"},"waterProtection":{"absenceModeEnabled":true,"pauseLeakageProtectionUntilUTC":"2026-06-10T14:16:00Z"},"mlState":"success"}'
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
            timestamp=datetime(2026, 6, 8, 13, 13, tzinfo=UTC),  
        ),
        water_protection=WaterProtectionResponse(
            absence_mode_enabled=True,
            pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16, tzinfo=UTC)
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
            "timestamp": "2026-06-08T13:13:00.0000000Z"
        },
        "waterProtection": {
            "absenceModeEnabled": true,
            "pauseLeakageProtectionUntilUTC": "2026-06-10T14:16:00.0000000Z"
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
                date=datetime(2026, 6, 10, tzinfo=UTC)
            ),
            StatisticsResponseEntry(
                consumption=234.5,
                date=datetime(2026, 6, 11, tzinfo=UTC)
            ),
        ]
    )
    json = '{"entries":[{"consumption":123.4,"date":"2026-06-10T00:00:00Z"},{"consumption":234.5,"date":"2026-06-11T00:00:00Z"}]}'
    assert res.model_dump_json() == json


def test_statistics_response_deserialize():
    res = StatisticsResponse(
        entries=[
            StatisticsResponseEntry(
                consumption=123.4,
                date=datetime(2026, 6, 10, tzinfo=UTC)
            ),
            StatisticsResponseEntry(
                consumption=234.5,
                date=datetime(2026, 6, 11, tzinfo=UTC)
            ),
        ]
    )
    json = """
    {
        "type": "statistics",
        "entries": [
            { "consumption": 123.4, "date": "2026-06-10T00:00:00.0000000Z" },
            { "consumption": 234.5, "date": "2026-06-11T00:00:00.0000000Z" }
        ]
    }
    """
    assert StatisticsResponse.model_validate_json(json) == res

def test_water_protection_response_serialize():
    res = WaterProtectionResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16, tzinfo=UTC)
    )
    json = '{"absenceModeEnabled":true,"pauseLeakageProtectionUntilUTC":"2026-06-10T14:16:00Z"}'
    assert res.model_dump_json() == json


def test_water_protection_response_deserialize():
    res = WaterProtectionResponse(
        absence_mode_enabled=True,
        pause_leakage_protection_until_utc=datetime(2026, 6, 10, 14, 16, tzinfo=UTC)
    )
    json = """
    {
        "absenceModeEnabled": true,
        "pauseLeakageProtectionUntilUTC": "2026-06-10T14:16:00.0000000Z"
    }
    """
    assert WaterProtectionResponse.model_validate_json(json) == res


def test_device_response_serialize():
    res = DeviceResponse(
        biocat_serial="2025001395300149",
        electronics_serial="2041730218",
        device_type_number="12000273",
        line="BIOCAT",
        series="KLS 3000-C",
        has_flow_rate_sensor=True,
        has_leakage_protection_system=True,
        has_lime_scale_protection=True,
        has_pressure_sensor=True,
        has_temperature_sensor=True,
        has_wireless_sensor_option=True,
        name="Schulungsgerät",
        current_firmware_version="V01.05.07",
        current_hardware_version="2",
        latest_firmware_version="V01.08.05",
        system_mac_address="00:A2:FF:01:EE:DE",
        ble_mac_address="CC:F9:57:8F:EE:C4"
    )
    json = '{"biocatSerial":"2025001395300149","electronicsSerial":"2041730218","deviceTypeNumber":"12000273","line":"BIOCAT","series":"KLS 3000-C","hasFlowRateSensor":true,"hasLeakageProtectionSystem":true,"hasLimeScaleProtection":true,"hasPressureSensor":true,"hasTemperatureSensor":true,"hasWirelessSensorOption":true,"name":"Schulungsgerät","currentFirmwareVersion":"V01.05.07","currentHardwareVersion":"2","latestFirmwareVersion":"V01.08.05","systemMacAddress":"00:A2:FF:01:EE:DE","bleMacAddress":"CC:F9:57:8F:EE:C4"}'
    assert res.model_dump_json() == json


def test_device_response_deserialize():
    res = DeviceResponse(
        biocat_serial="2025001395300149",
        electronics_serial="2041730218",
        device_type_number="12000273",
        line="BIOCAT",
        series="KLS 3000-C",
        has_flow_rate_sensor=True,
        has_leakage_protection_system=True,
        has_lime_scale_protection=True,
        has_pressure_sensor=True,
        has_temperature_sensor=True,
        has_wireless_sensor_option=True,
        name="Schulungsgerät",
        current_firmware_version="V01.05.07",
        current_hardware_version="2",
        latest_firmware_version="V01.08.05",
        system_mac_address="00:A2:FF:01:EE:DE",
        ble_mac_address="CC:F9:57:8F:EE:C4"
    )
    json = """
    {
        "biocatSerial": "2025001395300149",
        "electronicsSerial": "2041730218",
        "deviceTypeNumber": "12000273",
        "line": "BIOCAT",
        "series": "KLS 3000-C",
        "hasFlowRateSensor": true,
        "hasTemperatureSensor": true,
        "hasPressureSensor": true,
        "hasLimeScaleProtection": true,
        "hasLeakageProtectionSystem": true,
        "hasWirelessSensorOption": true,
        "name": "Schulungsgerät",
        "currentFirmwareVersion": "V01.05.07",
        "currentHardwareVersion": "2",
        "latestFirmwareVersion": "V01.08.05",
        "systemMacAddress": "00:A2:FF:01:EE:DE",
        "bleMacAddress": "CC:F9:57:8F:EE:C4"
    }
    """
    assert DeviceResponse.model_validate_json(json) == res

from typing import Annotated, Union
from pydantic import BaseModel, ConfigDict, Field


class DeviceResponse(BaseModel):
    """
    Represents a device.

    Attributes
    ----------
    bsn : str | None 
        Biocat device serial number.
    esn : str | None
        Device electronics serial number.
    device_type_number : str | None
        Device type product number.
    line : str | None 
        Product line.
    series : str | None 
        Product series.
    has_flow_rate_sensor: bool
        Whether this device has a water flow rate sensor.
    has_temperature_sensor: bool 
        Whether this device has a water temperature sensor.
    has_pressure_sensor: bool
        Whether this device has a water pressure sensor.
    has_lime_scale_protection: bool
        Whether this device has lime scale protection.
    has_leakage_protection_system: bool
        Whether this device has leakage protection.
    has_wireless_sensor_option: bool
        Whether this device supports wireless water detector sensors.
    name : str | None 
        Device name.
    current_firmware_version : str | None 
        Current device firmware version.
    current_hardware_version : str | None 
        Current device hardware version.
    latest_firmware_version : str | None 
        Latest available firmware version.
    system_mac_address : str | None 
        MAC address of the ethernet module.
    ble_mac_address : str | None
        MAC address of the BLE module.
    """

    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True, 
        validate_by_alias=True
    )

    biocat_serial:                 Annotated[Union[str, None], Field(alias='biocatSerial')]               = None
    electronics_serial:            Annotated[Union[str, None], Field(alias='electronicsSerial')]          = None
    device_type_number:            Annotated[Union[str, None], Field(alias='deviceTypeNumber')]           = None
    line:                          Annotated[Union[str, None], Field(alias='line')]                       = None
    series:                        Annotated[Union[str, None], Field(alias='series')]                     = None
    has_flow_rate_sensor:          Annotated[bool,             Field(alias='hasFlowRateSensor')]          = False
    has_temperature_sensor:        Annotated[bool,             Field(alias='hasTemperatureSensor')]       = False
    has_pressure_sensor:           Annotated[bool,             Field(alias='hasPressureSensor')]          = False
    has_lime_scale_protection:     Annotated[bool,             Field(alias='hasLimeScaleProtection')]     = False
    has_leakage_protection_system: Annotated[bool,             Field(alias='hasLeakageProtectionSystem')] = False
    has_wireless_sensor_option:    Annotated[bool,             Field(alias='hasWirelessSensorOption')]    = False
    name:                          Annotated[Union[str, None], Field(alias='name')]                       = None
    current_firmware_version:      Annotated[Union[str, None], Field(alias='currentFirmwareVersion')]     = None
    current_hardware_version:      Annotated[Union[str, None], Field(alias='currentHardwareVersion')]     = None
    latest_firmware_version:       Annotated[Union[str, None], Field(alias='latestFirmwareVersion')]      = None
    system_mac_address:            Annotated[Union[str, None], Field(alias='systemMacAddress')]           = None
    ble_mac_address:               Annotated[Union[str, None], Field(alias='bleMacAddress')]              = None

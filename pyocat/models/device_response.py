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
    line : str | None 
        Product line.
    series : str | None 
        Product series.
    name : str | None 
        Device name.
    current_firmware_version : str | None 
        Current device firmware version.
    latest_firmware_version : str | None 
        Latest available firmware version.
    """

    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True, 
        validate_by_alias=True
    )

    biocat_serial:            Annotated[Union[str, None], Field(alias='biocatSerial')]           = None
    electronics_serial:       Annotated[Union[str, None], Field(alias='electronicsSerial')]      = None
    line:                     Annotated[Union[str, None], Field(alias='line')]                   = None
    series:                   Annotated[Union[str, None], Field(alias='series')]                 = None
    name:                     Annotated[Union[str, None], Field(alias='name')]                   = None
    current_firmware_version: Annotated[Union[str, None], Field(alias='currentFirmwareVersion')] = None
    latest_firmware_version:  Annotated[Union[str, None], Field(alias='latestFirmwareVersion')]  = None

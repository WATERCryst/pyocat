from datetime import datetime
from typing import Annotated, Union
from pydantic import BaseModel, ConfigDict, Field


class WaterProtectionResponse(BaseModel):
    """
    Represents the current state of the water protection subsystem.

    Attributes
    ----------
    absence_mode_enabled : bool 
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : datetime
        UTC date time when the leakage protection will be active again.     
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    absence_mode_enabled:               Annotated[Union[bool,     None], Field(alias='absenceModeEnabled')]             = None
    pause_leakage_protection_until_utc: Annotated[Union[datetime, None], Field(alias='pauseLeakageProtectionUntilUTC')] = None

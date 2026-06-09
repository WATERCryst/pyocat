from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field


class MessageResponse(BaseModel):
    """
    Represents a message.

    Attributes
    ----------
    absence_mode_enabled : bool 
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : datetime
        UTC date time string when the leakage protection 
        will be active again.
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    absence_mode_enabled:               Annotated[bool,     Field(alias='absenceModeEnabled')]
    pause_leakage_protection_until_utc: Annotated[datetime, Field(alias='pauseLeakageProtectionUntilUTC')]

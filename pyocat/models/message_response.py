from dataclasses import dataclass
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field


@dataclass
class MessageResponse(BaseModel):
    """
    Represents a message.

    Attributes
    ----------
    type : str 
        Denotes the type of the response.
    absence_mode_enabled : bool 
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : datetime
        UTC date time string when the leakage protection 
        will be active again.
    """

    type:                               Annotated[str,      Field(alias='type')]
    absence_mode_enabled:               Annotated[bool,     Field(alias='absenceModeEnabled')]
    pause_leakage_protection_until_utc: Annotated[datetime, Field(alias='pauseLeakageProtectionUntilUTC')]

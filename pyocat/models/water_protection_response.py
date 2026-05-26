from dataclasses import dataclass
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field


@dataclass
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

    absence_mode_enabled:               Annotated[bool,     Field(alias='absenceModeEnabled')]
    pause_leakage_protection_until_utc: Annotated[datetime, Field(alias='pauseLeakageProtectionUntilUTC')]

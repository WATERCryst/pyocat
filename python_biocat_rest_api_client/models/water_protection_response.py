from datetime import datetime

from .base_response import BaseResponse


class WaterProtectionResponse(BaseResponse):
    """
    Represents the current state of the water protection subsystem.

    Attributes
    ----------
    absence_mode_enabled : bool 
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : datetime
        UTC date time when the leakage protection will be active again.     
    """

    absence_mode_enabled: bool
    pause_leakage_protection_until_utc: datetime

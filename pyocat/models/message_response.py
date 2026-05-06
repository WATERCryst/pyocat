from datetime import datetime

from .base_response import BaseResponse


class MessageResponse(BaseResponse):
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

    type: str
    absence_mode_enabled: bool
    pause_leakage_protection_until_utc: datetime

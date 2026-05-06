from datetime import datetime
from pydantic import BaseModel


class MessageResponse(BaseModel):
    """
    Represents a message.

    Attributes
    ----------
    type_ : str 
        Denotes the type of the response.
    absence_mode_enabled : bool 
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : datetime
        UTC date time string when the leakage protection 
        will be active again.
    """

    type_: str
    absence_mode_enabled: bool
    pause_leakage_protection_until_utc: datetime

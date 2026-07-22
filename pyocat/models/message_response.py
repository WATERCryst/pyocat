from typing import Annotated, Union
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class MessageResponse(BaseModel):
    """
    Represents a message.

    Attributes
    ----------
    absence_mode_enabled : bool | None
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : AwareDatetime | None
        UTC date time string when the leakage protection 
        will be active again.
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    absence_mode_enabled:               Annotated[Union[bool,     None],      Field(alias='absenceModeEnabled')]             = None
    pause_leakage_protection_until_utc: Annotated[Union[AwareDatetime, None], Field(alias='pauseLeakageProtectionUntilUTC')] = None

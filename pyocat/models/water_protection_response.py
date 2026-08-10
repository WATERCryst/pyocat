from typing import Annotated

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class WaterProtectionResponse(BaseModel):
    """
    Represents the current state of the water protection subsystem.

    Attributes
    ----------
    absence_mode_enabled : bool 
        Indicates the state of the absence mode.
    pause_leakage_protection_until_utc : AwareDatetime
        UTC date time when the leakage protection will be active again.     
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    absence_mode_enabled:               Annotated[bool          | None, Field(alias='absenceModeEnabled')]             = None
    pause_leakage_protection_until_utc: Annotated[AwareDatetime | None, Field(alias='pauseLeakageProtectionUntilUTC')] = None

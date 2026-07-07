from typing import Annotated, Literal, Union
from pydantic import BaseModel, ConfigDict, Field

from .event_response import EventResponse
from .mode_response import ModeResponse
from .water_protection_response import WaterProtectionResponse


MlState = Literal[ 
    "cancelled",
    "failure-pressure-drop",
    "failure-start-pressure",
    "failure-unknown",
    "failure-water-tap",
    "idle",
    "leakage",
    "running",
    "success"
]


class StateResponse(BaseModel):
    """
    Represents the current device state.

    Attributes
    ----------
    online : bool | None
        Indicates whether the device is online or offline right now.
    mode : ModeResponse | None
        Represents the current mode of operation.
    event : EventResponse | None
        Represents an event.
    water_protection : WaterProtectionResponse | None
        Represents the current state of the water protection subsystem. 
    ml_state : 'cancelled' | 'failure-pressure-drop' | 'failure-start-pressure' | 'failure-unknown' | 'failure-water-tap' | 'idle' | 'leakage' | 'running' | 'success' | None
        The state of the current (or last) micro leakage measurement.
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    online:           Annotated[Union[bool,                    None], Field(alias='online')]          = None
    mode:             Annotated[Union[ModeResponse,            None], Field(alias='mode')]            = None
    event:            Annotated[Union[EventResponse,           None], Field(alias='event')]           = None
    water_protection: Annotated[Union[WaterProtectionResponse, None], Field(alias='waterProtection')] = None
    ml_state:         Annotated[Union[MlState,                 None], Field(alias='mlState')]         = None

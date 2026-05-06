from typing import Literal
from pydantic import BaseModel

from .event_response import EventResponse
from .mode_response import ModeResponse
from .water_protection_response import WaterProtectionResponse


class StateResponse(BaseModel):
    """
    Represents the current device state.

    Attributes
    ----------
    online : bool 
        Indicates whether the device is online or offline right now.
    mode : ModeResponse
        Represents the current mode of operation.
    event : EventResponse
        Represents an event.
    water_protection : WaterProtectionResponse | None
        Represents the current state of the water protection subsystem. 
    ml_state : Literal["cancelled", "failure-pressure-drop", "failure-start-pressure", "failure-unknown", "failure-water-tap", "idle", "leakage", "running", "success"] | None
        The state of the current (or last) micro leakage measurement.
    """

    online: bool
    mode: ModeResponse
    event: EventResponse
    water_protection: WaterProtectionResponse | None
    ml_state: Literal[ 
        "cancelled",
        "failure-pressure-drop",
        "failure-start-pressure",
        "failure-unknown",
        "failure-water-tap",
        "idle",
        "leakage",
        "running",
        "success"
    ] | None

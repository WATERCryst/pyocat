from typing import Annotated, Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, PlainSerializer

from .event_response import EventResponse
from .mode_response import ModeResponse
from .water_protection_response import WaterProtectionResponse

ML_STATES = {
    "cancelled": "cancelled",
    "failure-pressure-drop": "failure_pressure_drop",
    "failure-start-pressure": "failure_start_pressure",
    "failure-unknown": "failure_unknown",
    "failure-water-tap": "failure_water_tap",
    "idle": "idle",
    "leakage": "leakage",
    "running": "running",
    "success": "success",
}
"""
ML states to python strings mapping.
"""

INVERSE_ML_STATES = {v: k for k, v in ML_STATES.items()}
"""
Python strings to ML states mapping.
"""

MlState = Literal[ 
    "cancelled",
    "failure_pressure_drop",
    "failure_start_pressure",
    "failure_unknown",
    "failure_water_tap",
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
    ml_state : MlState | None
        The state of the current (or last) micro leakage measurement.
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    online: Annotated[
        bool | None, 
        Field(alias='online')
    ] = None

    mode: Annotated[
        ModeResponse | None, 
        Field(alias='mode')
    ] = None

    event: Annotated[
        EventResponse | None, 
        Field(alias='event')
    ] = None

    water_protection: Annotated[
        WaterProtectionResponse | None, 
        Field(alias='waterProtection')
    ] = None

    ml_state: Annotated[
        MlState | None, 
        Field(alias='mlState'),
        BeforeValidator(lambda v: ML_STATES.get(v, v)),
        PlainSerializer(lambda v: INVERSE_ML_STATES.get(v, v))
    ] = None

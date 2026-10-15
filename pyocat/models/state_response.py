from enum import Enum
from typing import Annotated, Any, Dict

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, PlainSerializer

from .event_response import EventResponse
from .mode_response import ModeResponse
from .water_protection_response import WaterProtectionResponse

class MlState(str, Enum):
    CANCELLED = "cancelled"
    FAILURE_PRESSURE_DROP = "failure_pressure_drop"
    FAILURE_START_PRESSURE = "failure_start_pressure"
    FAILURE_UNKNOWN = "failure_unknown"
    FAILURE_WATER_TAP = "failure_water_tap"
    IDLE = "idle"
    LEAKAGE = "leakage"
    RUNNING = "running"
    SUCCESS = "success"


ML_STATES: Dict[str, MlState] = {
    "cancelled": MlState.CANCELLED,
    "failure-pressure-drop": MlState.FAILURE_PRESSURE_DROP,
    "failure-start-pressure": MlState.FAILURE_START_PRESSURE,
    "failure-unknown": MlState.FAILURE_UNKNOWN,
    "failure-water-tap": MlState.FAILURE_WATER_TAP,
    "idle": MlState.IDLE,
    "leakage": MlState.LEAKAGE,
    "running": MlState.RUNNING,
    "success": MlState.SUCCESS,
}
"""
ML states to python strings mapping.
"""

INVERSE_ML_STATES: Dict[MlState, str] = {v: k for k, v in ML_STATES.items()}
"""
Python strings to ML states mapping.
"""


def validate_ml_state(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, str) and v in ML_STATES:
        return ML_STATES[v]
    return v


def serialize_ml_state(v: MlState | None) -> str | None:
    if v is None:
        return None
    return INVERSE_ML_STATES.get(v)


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
        BeforeValidator(validate_ml_state),
        PlainSerializer(serialize_ml_state)
    ] = None

from enum import Enum
from typing import Annotated, Any, Dict

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, PlainSerializer

class ModeId(str, Enum):
    ERROR_MODE = "error_mode"
    FAIL_SAFE = "fail_safe"
    LEAKAGE_PROTECTION = "leakage_protection"
    MANUAL_CONTROL = "manual_control"
    RINSE = "rinse"
    SELF_TEST = "self_test"
    THERMAL_DISINFECTION = "thermal_disinfection"
    UPDATE = "update"
    WATER_OFF = "water_off"
    WATER_TREATMENT = "water_treatment"
"""
Specifies the current mode of operation.
"""

MODES: Dict[str, ModeId] = {
    "ER": ModeId.ERROR_MODE,
    "FS": ModeId.FAIL_SAFE,
    "LS": ModeId.LEAKAGE_PROTECTION,
    "MC": ModeId.MANUAL_CONTROL,
    "RS": ModeId.RINSE,
    "ST": ModeId.SELF_TEST,
    "TD": ModeId.THERMAL_DISINFECTION,
    "UD": ModeId.UPDATE,
    "WO": ModeId.WATER_OFF,
    "WT": ModeId.WATER_TREATMENT,
}
"""
Mode short codes to readable strings mapping.
"""

INVERSE_MODES: Dict[ModeId, str] = {v: k for k, v in MODES.items()}
"""
Mode readable strings to short code mapping.
"""


def validate_mode_id(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, str) and v in MODES:
        return MODES[v]
    return v


def serialize_mode_id(v: ModeId | None) -> str | None:
    if v is None:
        return None
    return INVERSE_MODES.get(v)


class ModeResponse(BaseModel):
    """
    Represents the current mode of operation.

    Attributes
    ----------
    id : ModeId | None
        Mode identifier.
    name : str | None
        Mode display name.
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    id: Annotated[
        ModeId | None, 
        Field(alias='id'), 
        BeforeValidator(validate_mode_id),
        PlainSerializer(serialize_mode_id)
    ] = None

    name: Annotated[
        str | None, 
        Field(alias='name')
    ] = None

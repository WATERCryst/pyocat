from typing import Annotated, Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, PlainSerializer

MODES = {
    "ER": "error_mode",
    "FS": "fail_safe",
    "LS": "leakage_protection",
    "MC": "manual_control",
    "RS": "rinse",
    "ST": "self_test",
    "TD": "thermal_disinfection",
    "UD": "update",
    "WO": "water_off",
    "WT": "water_treatment",
}
"""
Mode short codes to readable strings mapping.
"""

INVERSE_MODES = {v: k for k, v in MODES.items()}
"""
Mode readable strings to short code mapping.
"""

ModeId = Literal[
    "error_mode",
    "fail_safe",
    "leakage_protection",
    "manual_control",
    "rinse",
    "self_test",
    "thermal_disinfection",
    "update",
    "water_off",
    "water_treatment"
]
"""
Specifies the current mode of operation.
"""


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
        BeforeValidator(lambda v: MODES.get(v, v)),
        PlainSerializer(lambda v: INVERSE_MODES.get(v, v))
    ] = None

    name: Annotated[
        str | None, 
        Field(alias='name')
    ] = None

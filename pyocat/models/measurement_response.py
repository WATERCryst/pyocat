from typing import Annotated, Union
from pydantic import BaseModel, ConfigDict, Field


class MeasurementResponse(BaseModel):
    """
    Represents current measurement data.

    Attributes
    ----------
    water_temp : int | None
        Water temperature in degree celsius [°C].
    pressure : float | None
        Pressure in [bar].
    flow_rate : float | None 
        Flow rate in liters per minute [L/min].
    last_water_tap_volume : float | None
        Volume of the last water tapping in liters [L].
    last_water_tap_duration : float | None
        Duration of the last water tapping in seconds [sec].
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    water_temp:              Annotated[Union[int,   None], Field(alias='waterTemp')]            = None
    pressure:                Annotated[Union[float, None], Field(alias='pressure')]             = None
    flow_rate:               Annotated[Union[float, None], Field(alias='flowRate')]             = None
    last_water_tap_volume:   Annotated[Union[float, None], Field(alias='lastWaterTapVolume')]   = None
    last_water_tap_duration: Annotated[Union[int,   None], Field(alias='lastWaterTapDuration')] = None

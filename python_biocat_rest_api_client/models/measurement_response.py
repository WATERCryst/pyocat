from .base_response import BaseResponse


class MeasurementResponse(BaseResponse):
    """
    Represents current measurement data.

    Attributes
    ----------
    water_temp : int 
        Water temperature in degree celsius [°C].
    pressure : float
        Pressure in [bar].
    flow_rate : float 
        Flow rate in liters per minute [L/min].
    last_water_tap_volume : float
        Volume of the last water tapping in liters [L].
    last_water_tap_duration : float 
        Duration of the last water tapping in seconds [sec].
    """

    water_temp: int | None
    pressure: float | None
    flow_rate: float | None
    last_water_tap_volume: float | None
    last_water_tap_duration: float | None

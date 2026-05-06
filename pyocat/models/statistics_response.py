from datetime import datetime

from .base_response import BaseResponse


class StatisticsResponseEntry(BaseResponse):
    """
    A consumption statistics data point.

    Attributes
    ----------
    consumption : float 
        Water consumption for this day in liters [L].
    date : datetime 
        UTC date of the measurement. 
    """

    consumption: float
    date: datetime


class StatisticsResponse(BaseResponse):
    """
    Represents a list of consumption statistics data points.

    Attributes
    ----------
    type : str 
        Denotes the type of the response.
    entries : list[StatisticsResponseEntry] 
        List of data points.    
    """

    type: str
    entries: list[StatisticsResponseEntry] = []

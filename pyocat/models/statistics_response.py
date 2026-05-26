from dataclasses import dataclass
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field


@dataclass
class StatisticsResponseEntry(BaseModel):
    """
    A consumption statistics data point.

    Attributes
    ----------
    consumption : float 
        Water consumption for this day in liters [L].
    date : datetime 
        UTC date of the measurement. 
    """

    consumption: Annotated[float,    Field(alias='consumption')]
    date:        Annotated[datetime, Field(alias='date')]


@dataclass
class StatisticsResponse(BaseModel):
    """
    Represents a list of consumption statistics data points.

    Attributes
    ----------
    type : str 
        Denotes the type of the response.
    entries : list[StatisticsResponseEntry] 
        List of data points.    
    """

    type:    Annotated[str,                           Field(alias='type')]
    entries: Annotated[list[StatisticsResponseEntry], Field(alias='entries')] = []

from typing import Annotated

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class StatisticsResponseEntry(BaseModel):
    """
    A consumption statistics data point.

    Attributes
    ----------
    consumption : float | None
        Water consumption for this day in liters [L].
    date : AwareDatetime | None
        UTC date of the measurement. 
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    consumption: Annotated[float         | None, Field(alias='consumption')] = None
    date:        Annotated[AwareDatetime | None, Field(alias='date')]        = None


class StatisticsResponse(BaseModel):
    """
    Represents a list of consumption statistics data points.

    Attributes
    ----------
    entries : list[StatisticsResponseEntry] 
        List of data points.    
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    entries: Annotated[list[StatisticsResponseEntry], Field(alias='entries')] = []

from datetime import datetime
from typing import Annotated, Literal, Union
from pydantic import BaseModel, ConfigDict, Field


EventCategory = Literal['error', 'warning', 'info']


class EventResponse(BaseModel):
    """
    Represents an event.

    Attributes
    ----------
    event_id : int 
        Identifies the type of the event.
    category : Literal['error', 'warning', 'info'] 
        The event category.
    title : str 
        Event summary.
    description : str 
        Detailed description.
    timestamp : datetime
        UTC date time of the event.
    """

    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True, 
        validate_by_alias=True
    )

    event_id:    Annotated[int,                        Field(alias="eventId")]
    category:    Annotated[Union[EventCategory, None], Field(alias='category')]
    title:       Annotated[Union[str,           None], Field(alias='title')]
    description: Annotated[Union[str,           None], Field(alias='description')]
    timestamp:   Annotated[Union[datetime,      None], Field(alias='timestamp')]

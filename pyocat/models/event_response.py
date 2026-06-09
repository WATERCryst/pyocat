from datetime import datetime
from typing import Annotated, Literal
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

    event_id:    Annotated[int,           Field(alias="eventId")]
    category:    Annotated[EventCategory, Field(alias='category')]
    title:       Annotated[str,           Field(alias='title')]
    description: Annotated[str,           Field(alias='description')]
    timestamp:   Annotated[datetime,      Field(alias='timestamp')]

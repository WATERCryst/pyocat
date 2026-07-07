from datetime import datetime
from typing import Annotated, Literal, Union
from pydantic import BaseModel, ConfigDict, Field


EventCategory = Literal['error', 'warning', 'info']


class EventResponse(BaseModel):
    """
    Represents an event.

    Attributes
    ----------
    event_id : int | None
        Identifies the type of the event.
    category : 'error' | 'warning' | 'info' | None
        The event category.
    title : str | None
        Event summary.
    description : str | None
        Detailed description.
    timestamp : datetime | None
        UTC date time of the event.
    """

    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True, 
        validate_by_alias=True
    )

    event_id:    Annotated[Union[int,           None], Field(alias="eventId")]     = None
    category:    Annotated[Union[EventCategory, None], Field(alias='category')]    = None
    title:       Annotated[Union[str,           None], Field(alias='title')]       = None
    description: Annotated[Union[str,           None], Field(alias='description')] = None
    timestamp:   Annotated[Union[datetime,      None], Field(alias='timestamp')]   = None

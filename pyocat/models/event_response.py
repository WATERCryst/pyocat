from dataclasses import dataclass
from datetime import datetime
from typing import Annotated, Literal
from pydantic import BaseModel, Field


EventCategory = Literal['error', 'warning', 'info']


@dataclass
class EventResponse(BaseModel):
    """
    Represents an event.

    Attributes
    ----------
    type : str 
        Denotes the type of the response.
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

    type:        Annotated[str,           Field(alias='type')]
    event_id:    Annotated[int,           Field(alias='eventId')]
    category:    Annotated[EventCategory, Field(alias='category')]
    title:       Annotated[str,           Field(alias='title')]
    description: Annotated[str,           Field(alias='description')]
    timestamp:   Annotated[datetime,      Field(alias='timestamp')]

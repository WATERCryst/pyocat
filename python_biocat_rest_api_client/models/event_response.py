from datetime import datetime
from typing import Literal

from .base_response import BaseResponse


class EventResponse(BaseResponse):
    """
    Represents an event.

    Attributes
    ----------
    type_ : str 
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

    type_: str
    event_id: int
    category: Literal['error', 'warning', 'info']
    title: str
    description: str
    timestamp: datetime

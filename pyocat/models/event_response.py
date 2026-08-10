from typing import Annotated, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

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
    timestamp : AwareDatetime | None
        UTC date time of the event.
    """

    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True, 
        validate_by_alias=True
    )

    event_id:    Annotated[int           | None, Field(alias="eventId")]     = None
    category:    Annotated[EventCategory | None, Field(alias='category')]    = None
    title:       Annotated[str           | None, Field(alias='title')]       = None
    description: Annotated[str           | None, Field(alias='description')] = None
    timestamp:   Annotated[AwareDatetime | None, Field(alias='timestamp')]   = None

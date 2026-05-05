from pydantic import BaseModel


class StateResponse(BaseModel):
    """
    Represents the current device state.
    """

    online: bool

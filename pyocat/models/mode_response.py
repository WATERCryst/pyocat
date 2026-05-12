from typing import Annotated, Literal
from pydantic import BaseModel, Field


ModeId = Literal['ER', 'FS', 'MC', 'RS', 'ST', 'TD', 'UD', 'WO', 'WT']


class ModeResponse(BaseModel):
    """
    Represents the current mode of operation.

    Attributes
    ----------
    id : Literal['ER', 'FS', 'MC', 'RS', 'ST', 'TD', 'UD', 'WO', 'WT'] 
        Mode identifier.
    name : str 
        Mode display name.
    """

    id:   Annotated[ModeId, Field(alias='id')] 
    name: Annotated[str,    Field(alias='name')]

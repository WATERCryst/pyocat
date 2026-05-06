from typing import Literal
from pydantic import BaseModel


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

    id: Literal['ER', 'FS', 'MC', 'RS', 'ST', 'TD', 'UD', 'WO', 'WT']
    name: str

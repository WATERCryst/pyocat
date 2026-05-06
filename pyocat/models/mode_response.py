from typing import Literal

from .base_response import BaseResponse


class ModeResponse(BaseResponse):
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

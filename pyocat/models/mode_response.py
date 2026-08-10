from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

ModeId = Literal['ER', 'FS', 'LS', 'MC', 'RS', 'ST', 'TD', 'UD', 'WO', 'WT']
"""
Specifies the current mode of operation.

+------+----------------------------------+
| Mode | Description                      |
+------+----------------------------------+
| ER   | Error mode.                      |
+------+----------------------------------+
| FS   | Failsafe mode.                   |
+------+----------------------------------+
| LS   | Leakage protection.              |
+------+----------------------------------+
| MC   | Manual control.                  |
+------+----------------------------------+
| RS   | Rinse.                           |
+------+----------------------------------+
| ST   | Self test.                       |
+------+----------------------------------+
| TD   | Thermal disinfection.            |
+------+----------------------------------+
| UD   | Update.                          |
+------+----------------------------------+
| WO   | Water off.                       |
+------+----------------------------------+
| WT   | Water treatment.                 |
+------+----------------------------------+
"""


class ModeResponse(BaseModel):
    """
    Represents the current mode of operation.

    Attributes
    ----------
    id : 'ER' | 'FS' | 'LS' | 'MC' | 'RS' | 'ST' | 'TD' | 'UD' | 'WO' | 'WT' | None
        Mode identifier.
    name : str | None
        Mode display name.
    """

    model_config = ConfigDict(
        serialize_by_alias=True, 
        validate_by_name=True, 
        validate_by_alias=True
    )

    id:   Annotated[ModeId | None, Field(alias='id')]   = None
    name: Annotated[str    | None, Field(alias='name')] = None

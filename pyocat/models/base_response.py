import re

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

# Unfortunately some fields *UTC in the name.
# To match this with *_utc, first substitute
# utc with u_t_c the convert to camel case.
def my_to_camel(snake: str) -> str:
    snake = re.sub('utc', 'u_t_c', snake)
    return to_camel(snake)

class BaseResponse(BaseModel):
    model_config = ConfigDict(
        alias_generator=my_to_camel,
        populate_by_name=True,
        from_attributes=True,
    )
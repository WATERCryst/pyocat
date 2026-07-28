"""HTTP response helpers."""

from httpx import HTTPStatusError, Response

from .exceptions import (
    WTCApiDisabledError,
    WTCApiTemporaryError,
    WTCApiUnauthorizedError,
)


def raise_for_status(response: Response) -> None:
    """Translate HTTP errors into WATERCryst API errors."""
    try:
        response.raise_for_status()
    except HTTPStatusError as err:
        match err.response.status_code:
            case 401:
                raise WTCApiUnauthorizedError() from err
            case 403:
                raise WTCApiDisabledError() from err
            case status if status == 429 or status >= 500:
                raise WTCApiTemporaryError() from err
            case _:
                raise
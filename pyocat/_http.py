"""HTTP response helpers."""

from httpx2 import HTTPStatusError, Response

from .exceptions import (
    WTCApiDisabledError,
    WTCApiQuotaExceededError,
    WTCApiRequestError,
    WTCApiServerError,
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
            case 429:
                raise WTCApiQuotaExceededError() from err
            case status if status >= 500:
                raise WTCApiServerError() from err
            case _:
                raise WTCApiRequestError() from err
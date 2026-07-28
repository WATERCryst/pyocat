from typing import Mapping, Union

from httpx import Client, Response, HTTPStatusError

from pyocat.exceptions import WTCApiTemporaryError, WTCApiDisabledError, \
    WTCApiUnauthorizedError


class Auth:
    """
    Make authenticated requests.
    """

    def __init__(
        self,
        client: Client,
        api_key: str,
        host: str = 'https://appapi.watercryst.com'
    ):
        """
        Creates a new authenticated request sender.

        Parameters
        ----------
        client: `httpx.Client`
            Instance of a synchronous HTTP client.
        api_key : str
            The api key.
        host : str
            The Biocat SmartHome API host. 
            Defaults to `https://appapi.watercryst.com`.
        """
        self.client = client
        self.api_key = api_key
        self.host = host


    def get(
        self,
        path: str,
        params: Mapping[str, Union[str, int, float, bool]] | None = None,
    ) -> Response:
        """
        Send a `GET` request.

        Parameters
        ----------
        path : str
            The relative path.
        params : Mapping[str, Union[str, int, float, bool]]
            Optional query parameters. 

        Returns
        -------
        An `httpx.Response`.
        """
        headers = dict[str, str]()
        headers['X-API-KEY'] = self.api_key
        try:
            response = self.client.get(
                url=f'{self.host}/{path}',
                params=params,
                headers=headers
            )
            response.raise_for_status()
            return response
        except HTTPStatusError as err:
            match err.response.status_code:
                case 401:
                    raise WTCApiUnauthorizedError() from err
                case 403:
                    raise WTCApiDisabledError() from err
                case  status if status == 429 or status >= 500:
                    raise WTCApiTemporaryError() from err
                case _:
                    raise

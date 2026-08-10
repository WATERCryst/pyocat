from collections.abc import Mapping

from httpx import Client, Response

from ._http import raise_for_status


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
        params: Mapping[str, str | int | float | bool] | None = None,
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

        response = self.client.get(
            url=f'{self.host}/{path}',
            params=params,
            headers=headers
        )
        raise_for_status(response)
        return response

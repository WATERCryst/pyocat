from collections.abc import Mapping

from httpx import AsyncClient, Response

from ._http import raise_for_status


class AsyncAuth:
    """
    Make asynchronous authenticated requests.
    """

    def __init__(
            self,
            client: AsyncClient,
            api_key: str,
            host: str = 'https://appapi.watercryst.com'
    ):
        """
        Creates a new authenticated request sender.

        Parameters
        ----------
        client: `httpx.AsyncClient`
            Instance of an asynchronous HTTP client.
        api_key : str
            The api key.
        host : str
            The Biocat SmartHome API host. 
            Defaults to `https://appapi.watercryst.com`.
        """
        self.client = client
        self.api_key = api_key
        self.host = host

    async def get(
        self,
        path: str,
        params: Mapping[str, str | int | float | bool] | None = None,
    ) -> Response:
        """
        Send an asynchronous `GET` request.

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

        response = await self.client.get(
            url=f'{self.host}/{path}',
            params=params,
            headers=headers
        )
        raise_for_status(response)
        return response

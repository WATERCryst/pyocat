import httpx

from types import TracebackType
from typing import Literal, Mapping
from api_key_auth import ApiKeyAuth

from models import StateResponse
from models import MeasurementResponse


class BiocatRestApiClient:
    """
    TODO
    """

    # NOTE: DON'T add a slash at the end of the base url.
    _base_url = 'https://appapi.watercryst.com/v1'


    def __init__(self, key: str):
        auth = ApiKeyAuth(key)
        self._client = httpx.Client(auth=auth)


    def __enter__(self):
        self._client.__enter__()
        return self
    

    def __exit__(
        self, 
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None
    ):
        self._client.__exit__(exc_type, exc_value, traceback)
        return False


    def close(self):
        self._client.close()


    def acknowledge_event(self):
        """
        Acknowledges the current device warning or error.
        """
        pass


    def enable_absence(self):
        """
        Enables absence mode and raises leakage detector sensitivity.
        """
        pass


    def disable_absence(self):
        """
        Disables absence mode and reverts leakage detector 
        sensitivity to its default level.
        """
        pass


    def pause_leakage_protection(
        self, 
        minutes: int
    ):
        """
        Pauses leakage protection for a given duration of minutes.

        Parameters
        ----------
        minutes : int
            The pause duration in minutes. Must be within the range
            [1 .. 4320].
        """
        pass


    def unpause_leakage_protection(self):
        """
        Reactivates leakage protection.
        """
        pass


    def start_self_test(self):
        """
        Starts the self test routine. Automatically checks all 
        actuators and sensors and fills the active unit with drinking 
        water over a defined flushing time.
        
        Requires 2 minutes for completion. 
        
        The device will return to water treatment if no errors could 
        be detected.  
        
        In the case of errors, the current error will be reported
        via the webhook endpoint. Additionally it can be queried
        at any time with `GET v1/state`.        
        """
        pass


    def get_measurements(self) -> MeasurementResponse:
        """
        Fetches current measurement data.

        Returns
        -------
        The current measurement data.
        """
        response = self.get('measurements/direct')
        return MeasurementResponse.model_validate_json(response.json())


    def start_micro_leakage_measurement(self):
        """
        Starts the micro-leakage measurement to check the leak-
        tightness of the piping. This allows the detection of micro-
        leaks such as dripping taps or pipe fittings.  
        For this measurements, water supply is briefly shut off.
        
        An unexpected water consumption during the measuring process, 
        e.g. flushing the toilet or opening a tap, is automatically 
        detected and the water supply is restored within a few seconds.
        However, the test fails and the API call has to be repeated.
        
        ### Notice
        
        If you use a drip irrigation system in your household, this 
        can be detected as a micro leak.
        """
        pass


    def get_daily_statistics(self):
        """
        Fetches the daily statistics.
        """
        pass


    def get_todays_consumption(self) -> float:
        """
        Fetches the total consumption for today.
        """
        return 0


    def get_total_consumption(self) -> float:
        """
        Fetches the total water consumption since the device was 
        installed.
        """
        return 0


    def open_water_supply(self):
        """
        Connects the device with the water supply.
        Confirms pending warnings and errors.
        """
        pass


    def close_water_supply(self):
        """
        Disconnects the device from the water supply.
        """
        pass

    def get_state(
        self,
        locale: str = 'de',
        format: Literal['plain', 'md', 'html'] = 'plain'    
    ) -> StateResponse:
        """
        Returns the current state of the device.

        Parameters
        ----------
        locale : str
            The language of the event message. Defaults to `de`.
        format : `plain` | `md` | `html`
            The format of the event message. Defaults to `plain`.
            * `plain` - Renders the event message as plain text.
            * `md`    - Renders the event message as Markdown.
            * `html`  - Renders the event message as HTML.

        Returns
        -------
        The current device state.
        """
        response = self.get('state', { 'locale': locale, 'format': format })
        return StateResponse.model_validate_json(response.json())


    def get(
        self,
        path: str,
        params: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        """
        Send a `GET` request.

        Parameters
        ----------
        path : str
            The relative path.
        params : Mapping[str, str]
            Optional query parameters. 

        Returns
        -------
        An `httpx.Response`.
        """
        url = f'{self._base_url}/{path}'
        response = self._client.get(url, params=params)
        response.raise_for_status()
        return response

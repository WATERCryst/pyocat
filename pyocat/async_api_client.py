from typing import Literal

from .async_auth import AsyncAuth

from .models import MeasurementResponse
from .models import StatisticsResponse
from .models import StateResponse


class AsyncApiClient:
    """
    Asynchronous Biocat REST API v1 client.
    """

    def __init__(self, auth: AsyncAuth):
        self.auth = auth


    async def acknowledge_event(self):
        """
        Acknowledges the current device warning or error.
        """
        await self.auth.get('v1/ackevent')


    async def enable_absence(self):
        """
        Enables absence mode and raises leakage detector sensitivity.
        """
        await self.auth.get('v1/absence/enable')


    async def disable_absence(self):
        """
        Disables absence mode and reverts leakage detector 
        sensitivity to its default level.
        """
        await self.auth.get('v1/absence/disable')


    async def pause_leakage_protection(
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
        await self.auth.get('v1/leakageprotection/pause', { 'minutes': minutes })


    async def unpause_leakage_protection(self):
        """
        Reactivates leakage protection.
        """
        await self.auth.get('v1/leakageprotection/unpause')


    async def start_self_test(self):
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
        await self.auth.get('v1/selftest')


    async def get_measurements(self) -> MeasurementResponse:
        """
        Fetches current measurement data.

        Returns
        -------
        The current measurement data.
        """
        response = await self.auth.get('v1/measurements/direct')
        return MeasurementResponse.model_validate(response.json())


    async def start_micro_leakage_measurement(self):
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
        await self.auth.get('v1/mlmeasurement/start')


    async def get_daily_statistics(self) -> StatisticsResponse:
        """
        Fetches the daily statistics.

        Returns
        -------
        Water consumption statistics of the trailing 30 days.
        """
        response = await self.auth.get('v1/statistics/daily/direct')
        return StatisticsResponse.model_validate(response.json())


    async def get_todays_consumption(self) -> float:
        """
        Fetches the total consumption for today.

        Returns
        -------
        Todays total water consumption in [L].
        """
        response = await self.auth.get('v1/statistics/cumulative/daily')
        return float(response.json())


    async def get_total_consumption(self) -> float:
        """
        Fetches the total water consumption since the device was 
        installed.

        Returns
        -------
        Total water consumption in [L].
        """
        response = await self.auth.get('v1/statistics/cumulative/total')
        return float(response.json())


    async def open_water_supply(self):
        """
        Connects the device with the water supply.
        Confirms pending warnings and errors.
        """
        await self.auth.get('v1/watersupply/open')


    async def close_water_supply(self):
        """
        Disconnects the device from the water supply.
        """
        await self.auth.get('v1/watersupply/close')


    async def get_state(
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
        response = await self.auth.get(
            path='v1/state', 
            params={ 'locale': locale, 'format': format }
        )
        return StateResponse.model_validate(response.json())


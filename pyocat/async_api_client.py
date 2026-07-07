from .async_auth import AsyncAuth
from .async_client import AsyncClient, Formats, Locales
from .models import DeviceResponse
from .models import MeasurementResponse
from .models import StatisticsResponse
from .models import StateResponse


class AsyncApiClient(AsyncClient):
    """
    Asynchronous Biocat REST API v1 client.
    """

    def __init__(self, auth: AsyncAuth):
        self.auth = auth


    async def acknowledge_event(self):
        await self.auth.get('v1/ackevent')


    async def enable_absence(self):
        await self.auth.get('v1/absence/enable')


    async def disable_absence(self):
        await self.auth.get('v1/absence/disable')


    async def pause_leakage_protection(self, minutes: int):
        await self.auth.get(
            path='v1/leakageprotection/pause', 
            params={ 'minutes': minutes }
        )


    async def unpause_leakage_protection(self):
        await self.auth.get('v1/leakageprotection/unpause')


    async def start_self_test(self):
        await self.auth.get('v1/selftest')


    async def get_measurements(self):
        response = await self.auth.get('v1/measurements/direct')
        return MeasurementResponse.model_validate(response.json())


    async def start_micro_leakage_measurement(self):
        await self.auth.get('v1/mlmeasurement/start')


    async def get_daily_statistics(self):
        response = await self.auth.get('v1/statistics/daily/direct')
        return StatisticsResponse.model_validate(response.json())


    async def get_todays_consumption(self):
        response = await self.auth.get('v1/statistics/cumulative/daily')
        return float(response.json())


    async def get_total_consumption(self):
        response = await self.auth.get('v1/statistics/cumulative/total')
        return float(response.json())


    async def open_water_supply(self):
        await self.auth.get('v1/watersupply/open')


    async def close_water_supply(self):
        await self.auth.get('v1/watersupply/close')


    async def get_state(self,
        locale: Locales = 'de',
        format: Formats = 'plain'    
    ):
        response = await self.auth.get(
            path='v1/state', 
            params={ 'locale': locale, 'format': format }
        )
        return StateResponse.model_validate(response.json())


    async def get_device_info(self):
        response = await self.auth.get('v1/device')
        return DeviceResponse.model_validate(response.json())

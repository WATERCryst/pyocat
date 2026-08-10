from .auth import Auth
from .client import Client, Formats, Locales
from .models import (
    DeviceResponse,
    MeasurementResponse,
    StateResponse,
    StatisticsResponse,
)


class ApiClient(Client):
    """
    Synchronous Biocat REST API v1 client.
    """

    def __init__(self, auth: Auth):
        self.auth = auth


    def acknowledge_event(self):
        self.auth.get('v1/ackevent')


    def enable_absence(self):
        self.auth.get('v1/absence/enable')


    def disable_absence(self):
        self.auth.get('v1/absence/disable')


    def pause_leakage_protection(self, minutes: int):
        self.auth.get(
            path='v1/leakageprotection/pause', 
            params={ 'minutes': minutes }
        )


    def unpause_leakage_protection(self):
        self.auth.get('v1/leakageprotection/unpause')


    def start_self_test(self):
        self.auth.get('v1/selftest')


    def get_measurements(self):
        response = self.auth.get('v1/measurements/direct')
        return MeasurementResponse.model_validate(response.json())


    def start_micro_leakage_measurement(self):
        self.auth.get('v1/mlmeasurement/start')


    def get_daily_statistics(self):
        response = self.auth.get('v1/statistics/daily/direct')
        return StatisticsResponse.model_validate(response.json())


    def get_todays_consumption(self):
        response = self.auth.get('v1/statistics/cumulative/daily')
        return float(response.json())


    def get_total_consumption(self):
        response = self.auth.get('v1/statistics/cumulative/total')
        return float(response.json())


    def open_water_supply(self):
        self.auth.get('v1/watersupply/open')


    def close_water_supply(self):
        self.auth.get('v1/watersupply/close')


    def get_state(self,
        locale: Locales = 'de',
        format: Formats = 'plain'    
    ):
        response = self.auth.get(
            path='v1/state', 
            params={ 'locale': locale, 'format': format }
        )
        return StateResponse.model_validate(response.json())


    def get_device_info(self):
        response = self.auth.get('v1/device')
        return DeviceResponse.model_validate(response.json())

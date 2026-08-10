from abc import ABC, abstractmethod
from typing import Literal

from .models import (
    DeviceResponse,
    MeasurementResponse,
    StateResponse,
    StatisticsResponse,
)

type Locales = Literal['de', 'en', 'es', 'cs', 'da'] 
"""Supported locales."""

type Formats = Literal['plain', 'md', 'html']
"""Supported message output formats."""


class Client(ABC):
    """
    Synchronous Biocat client.
    """


    @abstractmethod
    def acknowledge_event(self):
        """
        Acknowledges the current device warning or error.
        """


    @abstractmethod
    def enable_absence(self):
        """
        Enables absence mode and raises leakage detector sensitivity.
        """


    @abstractmethod
    def disable_absence(self):
        """
        Disables absence mode and reverts leakage detector 
        sensitivity to its default level.
        """


    @abstractmethod
    def pause_leakage_protection(self, minutes: int):
        """
        Pauses leakage protection for a given duration of minutes.

        Parameters
        ----------
        minutes : int
            The pause duration in minutes. Must be within the range
            [1 .. 4320].
        """


    @abstractmethod
    def unpause_leakage_protection(self):
        """
        Reactivates leakage protection.
        """


    @abstractmethod
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


    @abstractmethod
    def get_measurements(self) -> MeasurementResponse:
        """
        Fetches current measurement data.

        Returns
        -------
        The current measurement data.
        """


    @abstractmethod
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


    @abstractmethod
    def get_daily_statistics(self) -> StatisticsResponse:
        """
        Fetches the daily statistics.

        Returns
        -------
        Water consumption statistics of the trailing 30 days.
        """


    @abstractmethod
    def get_todays_consumption(self) -> float:
        """
        Fetches the total consumption for today.

        Returns
        -------
        Todays total water consumption in [L].
        """


    @abstractmethod
    def get_total_consumption(self) -> float:
        """
        Fetches the total water consumption since the device was 
        installed.

        Returns
        -------
        Total water consumption in [L].
        """


    @abstractmethod
    def open_water_supply(self):
        """
        Connects the device with the water supply.
        Confirms pending warnings and errors.
        """


    @abstractmethod
    def close_water_supply(self):
        """
        Disconnects the device from the water supply.
        """


    @abstractmethod
    def get_state(self, 
        locale: Locales = 'de', 
        format: Formats = 'plain'
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


    @abstractmethod
    def get_device_info(self) -> DeviceResponse:
        """
        Returns general device information like the name, serial 
        numbers, model IDs and firmware version info.

        Returns
        -------
        General device information.
        """

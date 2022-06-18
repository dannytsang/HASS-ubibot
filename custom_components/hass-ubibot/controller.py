"""A demonstration 'hub' that connects several devices."""
from __future__ import annotations

# In a real implementation, this would be in an external library that's on PyPI.
# The PyPI package needs to be included in the `requirements` section of manifest.json
# See https://developers.home-assistant.io/docs/creating_integration_manifest
# for more information.
# This dummy hub always returns 3 rollers.
import asyncio
import random

from homeassistant.core import HomeAssistant


class Controller:
    """Interface to connecting to Ubibot."""

    def __init__(self, hass: HomeAssistant, api_key: str) -> None:
        """Init dummy channel device."""
        self._api_key = api_key
        self._hass = hass
        self.channels = [
            Channel(f"ubibot_1", f"1", self),
            Channel(f"ubibot_2", f"2", self),
            Channel(f"ubibot_3", f"3", self)
        ]
        self.online = True
    
    async def test_connection(self) -> bool:
        """Test connectivity to the Dummy hub is OK."""
        await asyncio.sleep(1)
        return True


class Channel:
    """Channel which represents a Ubibot device."""

    def __init__(self, channel_id: str, name: str, controller: Controller) -> None:
        """Init channel."""
        self._id = channel_id
        self._name = name
        self.controller = controller
        self._callbacks = set()

    @property
    def channel_id(self) -> str:
        """Return ID for Channel."""
        return self._id
    
    @property
    def name(self) -> str:
        """Return name for Channel."""
        return self._name
    
    def register_callback(self, callback: Callable[[], None]) -> None:
        """Register callback, called when Roller changes state."""
        self._callbacks.add(callback)

    def remove_callback(self, callback: Callable[[], None]) -> None:
        """Remove previously registered callback."""
        self._callbacks.discard(callback)
    
    @property
    def online(self) -> float:
        """Channel is online."""
        return True

    @property
    def battery_level(self) -> int:
        """Battery level as a percentage."""
        return random.randint(0, 100)
    
    @property
    def illuminance(self) -> int:
        """Return a sample illuminance in lux."""
        return random.randint(0, 500)
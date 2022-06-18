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
        self._name = host
        self._id = host.lower()
        self.rollers = [
            Roller(f"{self._id}_1", f"{self._name} 1", self),
            Roller(f"{self._id}_2", f"{self._name} 2", self),
            Roller(f"{self._id}_3", f"{self._name} 3", self),
        ]
        self.online = True


class Channel:
    """Channel which represents a Ubibot device."""

    def __init__(self, channel_id: str, name: str, controller: Controller) -> None:
        """Init dummy roller."""
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
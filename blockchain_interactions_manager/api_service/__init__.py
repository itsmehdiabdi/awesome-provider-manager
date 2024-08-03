from typing import Dict

from .arb import arb_api_services
from .base.interface import APIService
from .base.type import Config as ProviderConfig, Network
from .eth import eth_api_services

api_services: Dict[Network, APIService] = {
    "eth": eth_api_services,
    "arb": arb_api_services,
}

__all__ = ["APIService", "ProviderConfig", "api_services"]

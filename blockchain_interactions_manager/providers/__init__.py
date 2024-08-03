from typing import Dict

from .arb import arb_providers
from .base.interface import Provider as ProviderInterface
from .base.type import Config as ProviderConfig, Network
from .eth import eth_providers

providers: Dict[Network, ProviderInterface] = {
    "eth": eth_providers,
    "arb": arb_providers,
}

__all__ = ["ProviderInterface", "ProviderConfig", "providers"]

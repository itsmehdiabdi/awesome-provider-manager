from typing import Dict

from blockchain_interactions_manager.providers.eth import eth_providers
from blockchain_interactions_manager.providers.arb import arb_providers
from blockchain_interactions_manager.interfaces import Provider
from blockchain_interactions_manager.types import TypeNetwork

providers: Dict[TypeNetwork, Provider] = {"eth": eth_providers, "arb": arb_providers}

__all__ = ["providers"]

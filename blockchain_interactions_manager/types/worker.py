from typing import Dict, List

from blockchain_interactions_manager.types.provider import Config as ProviderConfig
from blockchain_interactions_manager.types.network import Network


Config = Dict[Network, List[ProviderConfig]]

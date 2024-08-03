from typing import Dict, List

from ...api_service import Network, APIServiceConfig

"""
    maps each network to its api_services' configs.
"""
Config = Dict[Network, List[APIServiceConfig]]

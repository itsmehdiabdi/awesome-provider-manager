from abc import abstractmethod
from typing import Dict

from blockchain_interactions_manager.handler import Handler
from blockchain_interactions_manager.types.network import Network
from blockchain_interactions_manager.types.strategy import Strategy
from blockchain_interactions_manager.utils import Singleton


class Worker(metaclass=Singleton):
    """
    Description
    ----------
    A worker knows handlers of all networks. (note that each network has just one handler)
    it resolves network and uses proper handler.

    Attributes
    ----------
    handlers: Dict[Network, Handler]
        maps each network to its handler.

    Methods
    -------
    get_balance(network: Network, strategy: Strategy, wallet_address: str):
        returns wallet_address's native balance.
    """

    handlers: Dict[Network, Handler]

    @abstractmethod
    def get_balance(
        self, network: Network, strategy: Strategy, wallet_address: str
    ) -> int:
        pass

from abc import abstractmethod
from typing import Dict

from ...handler import HandlerInterface
from ...api_service import Network
from ...strategies import StrategyType
from ...utils import Singleton


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

    handlers: Dict[Network, HandlerInterface]

    @abstractmethod
    def get_balance(
        self, network: Network, strategy: StrategyType, wallet_address: str
    ) -> int:
        pass

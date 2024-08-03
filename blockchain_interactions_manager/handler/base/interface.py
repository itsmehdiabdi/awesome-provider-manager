from abc import ABC, abstractmethod
from typing import List

from ...providers import ProviderInterface
from ...strategies import StrategyInterface


class Handler(ABC):
    """
    Description
    ----------
    A handler manages providers of a specific network. e.g. EthHandler manages ethereum providers.
    by knowing all providers of a network and all strategies, runs a specific function of its providers with the input strategy.
    it also resolves strategy type to its related object.

    Attributes
    ----------
    providers: List[ProviderInterface]
        all providers of a network.

    Methods
    -------
    def get_balance(self, strategy: StrategyInterface, wallet_address: str) -> int:
        returns wallet_address's native balance.
    """

    providers: List[ProviderInterface]

    @abstractmethod
    def get_balance(self, strategy: StrategyInterface, wallet_address: str) -> int:
        pass

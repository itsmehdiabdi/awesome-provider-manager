from typing import List
from abc import ABC, abstractmethod

from blockchain_interactions_manager.interfaces.provider import Provider
from blockchain_interactions_manager.types.strategy import Strategy


class Handler(ABC):
    """
    Description
    ----------
    A handler manages providers of a specific network. e.g. EthHandler manages ethereum providers.
    by knowing all providers of a network and all strategies, runs a specific function of its providers with the input strategy.  
    it also resolves strategy type to its related object.
    
    Attributes
    ----------
    providers: List[Provider]
        all providers of a network.

    Methods
    -------
    get_balance(strategy: Strategy, wallet_address: str):
        returns wallet_address's native balance.
    """

    providers: List[Provider]

    @abstractmethod
    def get_balance(self, strategy: Strategy, wallet_address: str) -> int:
        pass

from abc import ABC, abstractmethod
from typing import List

from ...api_service import APIService
from ...strategy import strategies, StrategyType
from ...strategy import StrategyInterface


class Handler(ABC):
    """
    Description
    ----------
    A handler manages api_services of a specific network. e.g. EthHandler manages ethereum api_services.
    by knowing all api_services of a network and all strategies, runs a specific function of its api_services with the input strategy.
    technically it's an api-service-hub.

    Attributes
    ----------
    api_services: List[APIService]
        all api_services of a network (handler).

    Methods
    -------
    def get_balance(self, strategy: StrategyInterface, wallet_address: str) -> int:
        it runs all providers' get_balance functions with the specified strategy.

        returns wallet_address's native balance.
    """

    api_services: List[APIService]

    @abstractmethod
    def get_balance(self, strategy: StrategyInterface, wallet_address: str) -> int:
        pass

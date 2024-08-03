from typing import List

from ..handler import HandlerInterface
from ..providers import ProviderInterface
from ..strategies import strategies, StrategyType


class Handler(HandlerInterface):
    def __init__(self, providers: List[ProviderInterface]) -> None:
        self.providers = providers

    def get_balance(self, strategy: StrategyType, wallet_address: str) -> int:
        response = strategies.get(strategy)[int]().run(
            [provider.get_balance for provider in self.providers], wallet_address
        )
        return response

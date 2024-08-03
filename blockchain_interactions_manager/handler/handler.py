from typing import List

from ..handler import HandlerInterface
from ..api_service import APIService
from ..strategy import strategies, StrategyType


class Handler(HandlerInterface):
    def __init__(self, providers: List[APIService]) -> None:
        self.providers = providers

    def get_balance(self, strategy: StrategyType, wallet_address: str) -> int:
        response = strategies.get(strategy)[int]().run(
            [provider.get_balance for provider in self.providers], wallet_address
        )
        return response

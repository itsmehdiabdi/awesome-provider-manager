from typing import List

from blockchain_interactions_manager.interfaces import (
    Provider,
    Handler as HandlerInterface,
)
from blockchain_interactions_manager.strategies import strategies
from blockchain_interactions_manager.types.strategy import Strategy


class Handler(HandlerInterface):
    def __init__(self, providers: List[Provider]) -> None:
        self.providers = providers

    def get_balance(self, strategy: Strategy, wallet_address: str) -> int:
        response = strategies.get(strategy)[int]().run(
            [provider.get_balance for provider in self.providers], wallet_address
        )
        return response

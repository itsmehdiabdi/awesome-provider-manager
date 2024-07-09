from blockchain_interactions_manager.interfaces import Connector
from blockchain_interactions_manager.worker.worker import Worker
from blockchain_interactions_manager.types import (
    TypeStrategy,
    TypeNetwork,
)


class LocalConnector(Connector):
    def __init__(self) -> None:
        self.worker = Worker()
        self.connection = "local"

    def get_balance(
        self, network: TypeNetwork, strategy: TypeStrategy, wallet_address: str
    ) -> int:
        return self.worker.get_balance(network, strategy, wallet_address)

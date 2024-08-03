from ..connector import ConnectorInterface
from ..api_service import Network
from ..strategies import StrategyType
from ..worker import Worker


class LocalConnector(ConnectorInterface):
    def __init__(self) -> None:
        self.worker = Worker()
        self.connection = "local"

    def get_balance(
        self, network: Network, strategy: StrategyType, wallet_address: str
    ) -> int:
        return self.worker.get_balance(network, strategy, wallet_address)

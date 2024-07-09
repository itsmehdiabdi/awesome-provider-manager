import os
import json

from blockchain_interactions_manager.interfaces.handler import Handler
from blockchain_interactions_manager.interfaces.worker import Worker as WorkerInterface
from blockchain_interactions_manager.providers import providers
from blockchain_interactions_manager.types.network import Network
from blockchain_interactions_manager.types.strategy import Strategy
from blockchain_interactions_manager.types.worker import Config
from blockchain_interactions_manager.handler import Handler


class Worker(WorkerInterface):

    def __init__(self) -> None:
        self.handlers = {}
        self.set_handlers()

    def get_balance(
        self, network: Network, strategy: Strategy, wallet_address: str
    ) -> int:
        response = self.get_handler(network).get_balance(strategy, wallet_address)
        return response

    def get_handler(self, network: Network) -> Handler:
        handler = self.handlers[network]
        return handler

    def set_handlers(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "./config.json")
        with open(config_path, "r", encoding="UTF-8") as f:
            configs: Config = json.load(f)
            for network in configs:
                self.handlers[network] = Handler(
                    [
                        providers[network][config["type"]](config["url"])
                        for config in configs[network]
                    ]
                )

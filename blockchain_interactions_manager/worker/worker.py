import os
import json

from ..handler import Handler, HandlerInterface
from ..providers import Network, providers
from ..strategies import StrategyType
from ..worker import WorkerConfig, WorkerInterface


class Worker(WorkerInterface):

    def __init__(self) -> None:
        self.handlers = {}
        self.set_handlers()

    def get_balance(
        self, network: Network, strategy: StrategyType, wallet_address: str
    ) -> int:
        response = self.get_handler(network).get_balance(strategy, wallet_address)
        return response

    def get_handler(self, network: Network) -> HandlerInterface:
        handler = self.handlers[network]
        return handler

    def set_handlers(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "./config.json")
        with open(config_path, "r", encoding="UTF-8") as f:
            configs: WorkerConfig = json.load(f)
            for network in configs:
                self.handlers[network] = Handler(
                    [
                        providers[network][config["type"]](config["url"])
                        for config in configs[network]
                    ]
                )

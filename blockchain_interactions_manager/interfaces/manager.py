from abc import ABC, abstractmethod

from blockchain_interactions_manager.types.network import Network
from blockchain_interactions_manager.types.requirement import Requirement
from blockchain_interactions_manager.types.manager import Config
from blockchain_interactions_manager.types.manager import Connectors


class Manager(ABC):
    """
    Description
    ----------
    A manager resolves requirement to connection type and strategy.
        e.g. it knows fastest requirement in ethereum network means local connection and fail-over strategy

    Attributes
    ----------
    network: Network
        specifies the network the manager belongs to
    connectors: Connectors
        maps each connector name to its object
    config : Config
        it maps requirement to connection type and strategy.

    Methods
    -------
    get_balance(requirement: Requirement, wallet_address: str) -> int:
        returns wallet_address's native balance.
    """

    network: Network
    connectors: Connectors
    config: Config

    @abstractmethod
    def get_balance(self, requirement: Requirement, wallet_address: str) -> int:
        pass

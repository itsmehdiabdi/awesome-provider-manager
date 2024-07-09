from typing import Dict

from blockchain_interactions_manager.strategies.fail_over import FailOver
from blockchain_interactions_manager.interfaces.strategy import Strategy
from blockchain_interactions_manager.types.strategy import Strategy as TypeStrategy

strategies: Dict[TypeStrategy, Strategy] = {"fail_over": FailOver}

__all__ = ["strategies"]

from typing import Dict

from .base.interface import Strategy as StrategyInterface
from .base.type import Strategy as StrategyType
from .fail_over import FailOver

strategies: Dict[StrategyType, StrategyInterface] = {"fail_over": FailOver}

__all__ = ["StrategyInterface", "StrategyType", "strategies"]

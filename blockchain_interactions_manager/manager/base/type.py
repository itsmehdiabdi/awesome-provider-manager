from typing import Dict, Literal, TypedDict

from ...connector import ConnectorInterface
from ...strategy import StrategyType

"""
    maps connector name to its object.
"""
Connectors = Dict[str, ConnectorInterface]

"""
    different types of requirement that app layer knows.
"""
Requirement = Literal["fastest"]


class RequirementConfig(TypedDict):
    """
    each requirement is translated to a connector and a strategy.
    we use this class for this clarification.

    Args:
        connector_name    (str): name of connector that must be used
        strategy (StrategyType): type of strategy that must be used
    """

    connector_name: str
    strategy: StrategyType


"""
    maps a requirement to its config (a connector and a strategy)
"""
ManagerConfig = Dict[Requirement, RequirementConfig]

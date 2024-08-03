from typing import Dict, Literal, TypedDict

from ...connectors import ConnectorInterface
from ...strategies import StrategyType

Connectors = Dict[str, ConnectorInterface]

Requirement = Literal["fastest"]


class RequirementConfig(TypedDict):
    connector_name: str
    strategy: StrategyType


ManagerConfig = Dict[Requirement, RequirementConfig]

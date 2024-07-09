from typing import Literal, TypedDict

from blockchain_interactions_manager.types.strategy import Strategy

Requirement = Literal["fastest"]


class Config(TypedDict):
    connector_name: str
    strategy: Strategy

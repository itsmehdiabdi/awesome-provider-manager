from typing import Dict

from blockchain_interactions_manager.types.requirement import (
    Config as RequirementConfig,
    Requirement,
)
from blockchain_interactions_manager.interfaces.connector import Connector

Config = Dict[Requirement, RequirementConfig]

Connectors = Dict[str, Connector]

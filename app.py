from blockchain_interactions_manager import (
    types,
    interfaces,
    connectors,
    Manager,
)

connectors_dict: types.TypeManagerConnectors = {"local1": connectors.LocalConnector()}
config: types.TypeManagerConfig = {
    "fastest": {"connector_name": "local1", "strategy": "fail_over"}
}
manager: interfaces.Manager = Manager("eth", connectors_dict, config)


balance: int = manager.get_balance(
    "fastest", "0xdf99A0839818B3f120EBAC9B73f82B617Dc6A555"
)
print(balance)

from blockchain_interactions_manager import (
    LocalConnector,
    ConnectorsType,
    ManagerInterface,
    ManagerConfig,
    Manager,
)

connectors_dict: ConnectorsType = {"local1": LocalConnector()}
config: ManagerConfig = {
    "fastest": {"connector_name": "local1", "strategy": "fail_over"}
}
manager: ManagerInterface = Manager("eth", connectors_dict, config)


balance: int = manager.get_balance(
    "fastest", "0xdf99A0839818B3f120EBAC9B73f82B617Dc6A555"
)
print(balance)

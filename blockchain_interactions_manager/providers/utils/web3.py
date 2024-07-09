from web3 import Web3

from blockchain_interactions_manager.interfaces import Provider


class Web3Provider(Provider):
    def __init__(self, rpc_provider) -> None:
        self.rpc_provider = rpc_provider
        self.w3 = Web3(Web3.HTTPProvider(rpc_provider))

    def get_balance(self, wallet_address: str) -> int:
        balance = self.w3.eth.get_balance(self.w3.toChecksumAddress(wallet_address))
        balance = self.w3.fromWei(balance, "ether")
        return balance
from web3 import Web3

from ..base.interface import APIService


class Web3APIService(APIService):
    def __init__(self, rpc_provider) -> None:
        self.rpc_provider = rpc_provider
        self.w3 = Web3(Web3.HTTPProvider(rpc_provider))

    def get_balance(self, wallet_address: str) -> int:
        balance = self.w3.eth.get_balance(self.w3.toChecksumAddress(wallet_address))
        balance = self.w3.fromWei(balance, "ether")
        return balance

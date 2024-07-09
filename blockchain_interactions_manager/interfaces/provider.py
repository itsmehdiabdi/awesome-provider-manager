from abc import ABC, abstractmethod


class Provider(ABC):
    """
    Description
    ----------
    A provider handles an api for a specific network. e.g. EthWeb3Provider handles web3 ethereum apis.

    Attributes
    ----------
    rpc_provider : str
        the url of the api that a provider handles

    Methods
    -------
    get_balance(wallet_address: str):
        returns wallet_address's native balance.
    """

    rpc_provider: str

    @abstractmethod
    def get_balance(self, wallet_address: str) -> int:
        pass

# add some flags like:
#   privacy issue
#   free

# support rate limit handling

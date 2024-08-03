from abc import ABC, abstractmethod


class APIService(ABC):
    """
    Description
    ----------
    An api_service handles an api for a specific network. e.g. EthWeb3APIService handles web3 ethereum apis.

    Attributes
    ----------
    rpc_provider : str
        the url of the api that an api_service handles

    Methods
    -------
    get_balance(wallet_address: str):
        it's a wrapper on requesting to the api.

        returns wallet_address's native balance.
    """

    rpc_provider: str

    @abstractmethod
    def get_balance(self, wallet_address: str) -> int:
        pass

# TODO:
# add some flags like:
#   privacy issue
#   free

# support rate limit handling

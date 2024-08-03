from typing import Literal, TypedDict


class Config(TypedDict):
    """
    Args:
        type (str): clarifies which APIService class handles its api. e.g. Web3, graphql, ...
        url  (str): full-node address
    """
    type: str
    url: str


Network = Literal["eth", "arb"]

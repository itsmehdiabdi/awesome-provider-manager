from typing import Literal, TypedDict


class Config(TypedDict):
    type: str
    url: str


Network = Literal["eth", "arb"]

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable, List

T = TypeVar("T")


class Strategy(ABC, Generic[T]):
    """
    Description
    ----------
    A strategy runs some functions with a defined strategy. e.g. fail-over, parallel, ... .

    Methods
    -------
    run(functions: List[Callable], **kwargs):
        it runs all input functions based on run's implementation.
    """

    @classmethod
    @abstractmethod
    def run(cls, functions: List[Callable], **kwargs) -> T:
        pass

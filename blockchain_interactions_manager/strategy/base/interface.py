from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable, List

T = TypeVar("T")


class Strategy(ABC, Generic[T]):
    """
    Description
    ----------
    A strategy runs the input functions with the implemented strategy. e.g. fail-over, parallel, ... .

    Methods
    -------
    run(functions: List[Callable], **kwargs):
        it runs all input functions based on run's implementation.
        note that all functions must have the same signatures.
    """

    @classmethod
    @abstractmethod
    def run(cls, functions: List[Callable], **kwargs) -> T:
        pass

import abc
from typing import List, Dict, Any


class DBProviderInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get') and
                callable(subclass.getData) and
                hasattr(subclass, 'save') and
                callable(subclass.putData) or
                NotImplemented)

    @abc.abstractmethod
    def get(self, tblName: str, columns: List[str]):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, data: Dict[str, Any]):
        """Extract text from the data set"""
        raise NotImplementedError

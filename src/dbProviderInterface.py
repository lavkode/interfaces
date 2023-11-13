import abc
from typing import List, Dict


class DBProviderInterface(abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'getData') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'putData') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    @abc.abstractmethod
    def getData(self, tblName: str, columns: List[str]):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def putData(self, data: Dict[str]):
        """Extract text from the data set"""
        raise NotImplementedError
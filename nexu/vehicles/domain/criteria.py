from abc import ABC, abstractmethod


class Criteria(ABC):
    @abstractmethod
    def filter(self, buffer):
        pass

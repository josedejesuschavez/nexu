from abc import ABC, abstractmethod
from typing import List


class Criteria(ABC):
    @abstractmethod
    def filter(self, buffer):
        pass

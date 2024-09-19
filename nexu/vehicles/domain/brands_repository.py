from abc import ABC, abstractmethod
from typing import List

from vehicles.domain.brand import Brand


class BrandsRepository(ABC):

    @abstractmethod
    def get_all_brands(self) -> List[Brand]:
        pass

    @abstractmethod
    def get_brand_by_id(self, brand_id: int) -> Brand:
        pass

    @abstractmethod
    def insert_brand(self, name: str):
        pass

    @abstractmethod
    def update_average_price(self, brand_id: int, average_price: int):
        pass
from abc import ABC, abstractmethod

from vehicles.domain.criteria import Criteria
from vehicles.domain.model import Model


class ModelsRepository(ABC):
    @abstractmethod
    def get_all_models(
        self,
        greater: str,
        lower: str,
        greater_than_criteria: Criteria,
        less_than_criteria: Criteria,
    ):
        pass

    @abstractmethod
    def get_models_by_brand_name(self, brand_name: str):
        pass

    @abstractmethod
    def get_model_by_id(self, model_id: int) -> Model:
        pass

    @abstractmethod
    def insert_model(self, brand_name: str, name: str, average_price: int):
        pass

    @abstractmethod
    def update_average_price(self, model_id: int, average_price: int):
        pass

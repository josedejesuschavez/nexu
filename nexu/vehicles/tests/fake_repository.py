from typing import List

from vehicles.domain.brand import Brand
from vehicles.domain.brands_repository import BrandsRepository
from vehicles.domain.criteria import Criteria
from vehicles.domain.model import Model
from vehicles.domain.models_repository import ModelsRepository


class ModelsRepositoryTest(ModelsRepository):
    def get_all_models(
        self,
        greater: str,
        lower: str,
        greater_than_criteria: Criteria,
        less_than_criteria: Criteria,
    ):
        pass

    def get_models_by_brand_name(self, brand_name: str):
        return [
            Model.create_model(
                model_id=1, name="test", average_price=100000, brand_name=brand_name
            ),
            Model.create_model(
                model_id=2, name="test", average_price=100000, brand_name=brand_name
            ),
            Model.create_model(
                model_id=3, name="test", average_price=100000, brand_name=brand_name
            ),
            Model.create_model(
                model_id=4, name="test", average_price=100000, brand_name=brand_name
            ),
            Model.create_model(
                model_id=5, name="test", average_price=100000, brand_name=brand_name
            ),
        ]

    def get_model_by_id(self, model_id: int) -> Model:
        pass

    def insert_model(self, brand_name: str, name: str, average_price: int):
        pass

    def update_average_price(self, model_id: int, average_price: int):
        pass


class BrandsRepositoryTest(BrandsRepository):
    def get_all_brands(self) -> List[Brand]:
        return [
            Brand.create_brand(brand_id=1, name="test", average_price=5),
            Brand.create_brand(brand_id=2, name="test", average_price=5),
            Brand.create_brand(brand_id=3, name="test", average_price=5),
            Brand.create_brand(brand_id=4, name="test", average_price=5),
            Brand.create_brand(brand_id=5, name="test", average_price=5),
            Brand.create_brand(brand_id=6, name="test", average_price=5),
        ]

    def get_brand_by_id(self, brand_id: int) -> Brand:
        return Brand.create_brand(brand_id=brand_id, name="test", average_price=5)

    def insert_brand(self, name: str):
        pass

    def update_average_price(self, brand_id: int, average_price: int):
        pass

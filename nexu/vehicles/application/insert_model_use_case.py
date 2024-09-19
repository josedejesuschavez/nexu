from vehicles.application.get_brand_by_id_use_case import GetBrandByIdUseCase
from vehicles.application.update_average_price_by_brand_id_use_case import (
    UpdateAveragePriceByBrandIdUseCase,
)
from vehicles.domain.brands_repository import BrandsRepository
from vehicles.domain.model import Model
from vehicles.domain.models_repository import ModelsRepository


class InsertModelUseCase:
    def __init__(
        self, models_repository: ModelsRepository, brands_repository: BrandsRepository
    ):
        self.models_repository = models_repository
        self.brands_repository = brands_repository

    def execute(self, brand_id: int, name: str, average_price: int):
        get_brand_by_id_use_case = GetBrandByIdUseCase(
            brands_repository=self.brands_repository
        )
        brand = get_brand_by_id_use_case.execute(brand_id=brand_id)
        models = self.models_repository.get_models_by_brand_name(brand_name=brand.name)
        Model.verify_if_model_exists(name=name, models=models)
        self.models_repository.insert_model(
            brand_name=brand.name, name=name, average_price=average_price
        )

        price_total = sum([model.average_price for model in models]) + average_price
        count_model = len(models) + 1

        current_average_price = int(price_total / count_model)

        update_average_price_by_brand_id_use_case = UpdateAveragePriceByBrandIdUseCase(
            brands_repository=self.brands_repository
        )
        update_average_price_by_brand_id_use_case.execute(
            brand_id=brand_id, average_price=current_average_price
        )

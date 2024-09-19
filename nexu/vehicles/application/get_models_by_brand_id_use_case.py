from vehicles.application.get_brand_by_id_use_case import GetBrandByIdUseCase
from vehicles.domain.brands_repository import BrandsRepository
from vehicles.domain.models_repository import ModelsRepository


class GetModelsByBrandIdUseCase:

    def __init__(self, models_repository: ModelsRepository, brands_repository: BrandsRepository):
        self.models_repository = models_repository
        self.brands_repository = brands_repository

    def execute(self, brand_id: int):
        get_brand_by_id_use_case = GetBrandByIdUseCase(brands_repository=self.brands_repository)
        brand = get_brand_by_id_use_case.execute(brand_id=brand_id)
        models = self.models_repository.get_models_by_brand_name(brand_name=brand.name)
        models_dict = [model.to_dict() for model in models]
        return models_dict

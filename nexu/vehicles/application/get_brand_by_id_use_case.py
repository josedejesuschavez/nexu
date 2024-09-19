from vehicles.domain.brands_repository import BrandsRepository


class GetBrandByIdUseCase:

    def __init__(self, brands_repository: BrandsRepository):
        self.brands_repository = brands_repository

    def execute(self, brand_id: int):
        return self.brands_repository.get_brand_by_id(brand_id=brand_id)

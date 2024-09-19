from vehicles.domain.brand import Brand
from vehicles.domain.brands_repository import BrandsRepository


class InsertBrandUseCase:
    def __init__(self, brands_repository: BrandsRepository):
        self.brands_repository = brands_repository

    def execute(self, name: str):
        brands = self.brands_repository.get_all_brands()
        Brand.verify_if_brand_exists(name=name, brands=brands)
        self.brands_repository.insert_brand(name=name)

from vehicles.domain.brands_repository import BrandsRepository


class GetAllBrandsUseCase:

    def __init__(self, brands_repository: BrandsRepository):
        self.brands_repository = brands_repository

    def execute(self):
        brands = self.brands_repository.get_all_brands()
        return [brand.to_dict() for brand in brands]

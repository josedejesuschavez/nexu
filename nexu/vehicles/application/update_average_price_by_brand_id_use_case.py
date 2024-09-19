from vehicles.domain.brands_repository import BrandsRepository


class UpdateAveragePriceByBrandIdUseCase:
    def __init__(self, brands_repository: BrandsRepository):
        self.brands_repository = brands_repository

    def execute(self, brand_id: int, average_price: int):
        self.brands_repository.update_average_price(
            brand_id=brand_id, average_price=average_price
        )

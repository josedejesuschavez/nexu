from typing import List

from vehicles.domain.brand import Brand
from vehicles.domain.brands_repository import BrandsRepository
from vehicles.models import BrandModel


class SQLBrandsRepository(BrandsRepository):
    def get_all_brands(self) -> List[Brand]:
        data = BrandModel.objects.all()
        brands = [
            Brand.create_brand(
                brand_id=i.id, name=i.name, average_price=i.average_price
            )
            for i in data
        ]
        return brands

    def get_brand_by_id(self, brand_id: int) -> Brand:
        filtered_brands = BrandModel.objects.filter(id=brand_id).first()

        if filtered_brands:
            return Brand.create_brand(
                brand_id=filtered_brands.id,
                name=filtered_brands.name,
                average_price=filtered_brands.average_price,
            )
        return Brand.create_brand(brand_id=0, name="", average_price=0)

    def insert_brand(self, name: str):
        BrandModel(name=name, average_price=0).save()

    def update_average_price(self, brand_id: int, average_price: int):
        BrandModel.objects.filter(id=brand_id).update(average_price=average_price)

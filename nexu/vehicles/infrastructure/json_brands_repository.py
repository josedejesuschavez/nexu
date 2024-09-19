import json
import os
from typing import List

from vehicles.domain.brand import Brand
from vehicles.domain.brands_repository import BrandsRepository


class JSONBrandsRepository(BrandsRepository):

    def __init__(self):
        pass

    def load_data(self):
        if os.path.exists('brands.json'):
            with open('brands.json', 'r') as file:
                return json.load(file)
        return []

    def save_data(self, data):
        with open('brands.json', 'w') as file:
            json.dump(data, file, indent=4)

    def get_all_brands(self) -> List[Brand]:
        data = self.load_data()
        brands = [Brand.create_brand(brand_id=i['id'], name=i['nombre'], average_price=i['average_price']) for i in data]
        return brands

    def get_brand_by_id(self, brand_id: int) -> Brand:
        data = self.load_data()
        filtered_brands = list(filter(lambda brand: brand.get('id') == brand_id, data))

        if filtered_brands:
            return Brand.create_brand(brand_id=filtered_brands[0].get('id'), name=filtered_brands[0].get('nombre'), average_price=filtered_brands[0].get('average_price'))
        return Brand.create_brand(brand_id=0, name='', average_price=0)

    def insert_brand(self, name: str):
        data = self.load_data()
        max_id = max(data, key=lambda x: x['id'])['id']
        new_brand = Brand.create_brand(brand_id=max_id+1, name=name, average_price=0)
        data.append(new_brand.to_dict())
        self.save_data(data)

    def update_average_price(self, brand_id: int, average_price: int):
        data = self.load_data()
        for item in data:
            if item["id"] == brand_id:
                item["average_price"] = average_price
                break

        self.save_data(data)
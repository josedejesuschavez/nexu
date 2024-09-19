from typing import List


class Brand:
    def __init__(self, brand_id: int, name: str, average_price: int):
        self.brand_id = brand_id
        self.name = name
        self.average_price = average_price
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("Invalid brand data provided.")

    @classmethod
    def create_brand(cls, brand_id: int, name: str, average_price: int):
        return cls(brand_id=brand_id, name=name, average_price=average_price)

    @staticmethod
    def verify_if_brand_exists(name: str, brands: List["Brand"]):
        filtered_brands = list(
            filter(lambda brand: brand.name.upper() == name.upper(), brands)
        )

        if filtered_brands:
            raise ValueError(f"A brand with the name '{name}' already exists.")

    def to_dict(self):
        return {
            "id": self.brand_id,
            "nombre": self.name,
            "average_price": self.average_price,
        }

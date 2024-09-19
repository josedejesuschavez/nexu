from typing import List


class Model:
    def __init__(self, model_id: int, name: str, average_price: int, brand_name: str):
        self.model_id = model_id
        self.name = name
        self.average_price = average_price
        self.brand_name = brand_name
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("Invalid model data provided.")

        if self.average_price < 100000:
            raise ValueError("The average_price must be greater then 100,000.")

    @classmethod
    def create_model(
        cls, model_id: int, name: str, average_price: int, brand_name: str
    ):
        return cls(
            model_id=model_id,
            name=name,
            average_price=average_price,
            brand_name=brand_name,
        )

    @staticmethod
    def verify_if_model_exists(name: str, models: List["Model"]):
        filtered_models = list(
            filter(lambda model: model.name.upper() == name.upper(), models)
        )

        if filtered_models:
            raise ValueError(f"A model with the name '{name}' already exists.")

    def to_dict(self):
        return {
            "id": self.model_id,
            "name": self.name,
            "average_price": self.average_price,
            "brand_name": self.brand_name,
        }

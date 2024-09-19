import json
import os
from typing import List

from vehicles.domain.criteria import Criteria
from vehicles.domain.model import Model
from vehicles.domain.models_repository import ModelsRepository


class JSONModelsRepository(ModelsRepository):

    def __init__(self):
        pass

    def load_data(self):
        if os.path.exists('models.json'):
            with open('models.json', 'r') as file:
                return json.load(file)
        return []

    def save_data(self, data):
        with open('models.json', 'w') as file:
            json.dump(data, file, indent=4)

    def get_all_models(self, greater: str, lower: str, greater_than_criteria: Criteria, less_than_criteria: Criteria):
        data = self.load_data()

        if lower:
            data = less_than_criteria.filter(data)

        if greater:
            data = greater_than_criteria.filter(data)

        models = [{ 'id': i['id'], 'name': i['name'], 'average_price': i['average_price'] } for i in data]
        return models

    def get_models_by_brand_name(self, brand_name: str):
        data = self.load_data()
        filtered_data = list(filter(lambda model: model.get('brand_name').upper() == brand_name.upper(), data))
        models = [Model.create_model(model_id=i['id'], name=i['name'], average_price=i['average_price'], brand_name=brand_name) for i in filtered_data]
        return models

    def get_model_by_id(self, model_id: int) -> Model:
        data = self.load_data()
        filtered_models = list(filter(lambda model: model.get('id') == model_id, data))

        if filtered_models:
            return Model.create_model(model_id=filtered_models[0].get('id'), name=filtered_models[0].get('name'), average_price=filtered_models[0].get('average_price'), brand_name=filtered_models[0].get('brand_name'))
        return Model.create_model(model_id=0, name='', average_price=0, brand_name='')

    def insert_model(self, brand_name: str, name: str, average_price: int):
        data = self.load_data()
        max_id = max(data, key=lambda x: x['id'])['id']
        new_model = Model.create_model(model_id=max_id+1, name=name, average_price=average_price, brand_name=brand_name)
        data.append(new_model.to_dict())
        self.save_data(data)

    def update_average_price(self, model_id: int, average_price: int):
        data = self.load_data()
        for item in data:
            if item["id"] == model_id:
                item["average_price"] = average_price
                break

        self.save_data(data)

from vehicles.domain.criteria import Criteria
from vehicles.domain.model import Model
from vehicles.domain.models_repository import ModelsRepository
from vehicles.models import ModelModel, BrandModel


class SQLModelsRepository(ModelsRepository):
    def get_all_models(
        self,
        greater: str,
        lower: str,
        greater_than_criteria: Criteria,
        less_than_criteria: Criteria,
    ):
        data = ModelModel.objects.all()
        if lower:
            data = less_than_criteria.filter(data)

        if greater:
            data = greater_than_criteria.filter(data)

        models = [
            {"id": i.id, "name": i.name, "average_price": i.average_price} for i in data
        ]
        return models

    def get_models_by_brand_name(self, brand_name: str):
        filtered_data = ModelModel.objects.filter(brand__name__iexact=brand_name)
        models = [
            Model.create_model(
                model_id=i.id,
                name=i.name,
                average_price=i.average_price,
                brand_name=brand_name,
            )
            for i in filtered_data
        ]
        return models

    def get_model_by_id(self, model_id: int) -> Model:
        filtered_models = ModelModel.objects.filter(id=model_id)
        if filtered_models:
            return Model.create_model(
                model_id=filtered_models[0].id,
                name=filtered_models[0].name,
                average_price=filtered_models[0].average_price,
                brand_name=filtered_models[0].brand.name,
            )
        return Model.create_model(model_id=0, name="", average_price=0, brand_name="")

    def insert_model(self, brand_name: str, name: str, average_price: int):
        filtered_data = BrandModel.objects.filter(name__iexact=brand_name).first()
        ModelModel(name=name, average_price=average_price, brand=filtered_data).save()

    def update_average_price(self, model_id: int, average_price: int):
        ModelModel.objects.filter(id=model_id).update(average_price=average_price)

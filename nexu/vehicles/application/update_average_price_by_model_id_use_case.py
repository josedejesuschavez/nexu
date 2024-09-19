from vehicles.application.get_model_by_id_use_case import GetModelByIdUseCase
from vehicles.domain.models_repository import ModelsRepository


class UpdateAveragePriceByModelId:
    def __init__(self, models_repository: ModelsRepository):
        self.models_repository = models_repository

    def execute(self, model_id: int, average_price: int):
        get_model_by_id_use_case = GetModelByIdUseCase(self.models_repository)
        model = get_model_by_id_use_case.execute(model_id=model_id)
        model.average_price = average_price
        self.models_repository.update_average_price(
            model_id=model_id, average_price=average_price
        )

from vehicles.domain.models_repository import ModelsRepository


class GetModelByIdUseCase:
    def __init__(self, models_repository: ModelsRepository):
        self.models_repository = models_repository

    def execute(self, model_id):
        return self.models_repository.get_model_by_id(model_id=model_id)

from vehicles.domain.criteria import Criteria
from vehicles.domain.models_repository import ModelsRepository


class GetAllModelsUseCase:
    def __init__(
        self,
        models_repository: ModelsRepository,
        greater_than_criteria: Criteria,
        less_than_criteria: Criteria,
    ):
        self.models_repository = models_repository
        self.greater_than_criteria = greater_than_criteria
        self.less_than_criteria = less_than_criteria

    def execute(self, greater: str, lower: str):
        return self.models_repository.get_all_models(
            greater=greater,
            lower=lower,
            greater_than_criteria=self.greater_than_criteria,
            less_than_criteria=self.less_than_criteria,
        )

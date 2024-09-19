from vehicles.application.get_models_by_brand_id_use_case import (
    GetModelsByBrandIdUseCase,
)
from vehicles.tests.fake_repository import ModelsRepositoryTest
from vehicles.tests.test_brand import BrandsRepositoryTest


def test_get_models_by_brand_id():
    brand_id = 1
    use_case = GetModelsByBrandIdUseCase(
        models_repository=ModelsRepositoryTest(),
        brands_repository=BrandsRepositoryTest(),
    )

    result = use_case.execute(brand_id=brand_id)

    assert len(result) == 5

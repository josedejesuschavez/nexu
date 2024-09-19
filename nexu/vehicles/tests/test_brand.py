from vehicles.application.get_all_brands_use_case import GetAllBrandsUseCase
from vehicles.tests.fake_repository import BrandsRepositoryTest


def test_get_all_brands():
    use_case = GetAllBrandsUseCase(brands_repository=BrandsRepositoryTest())

    result = use_case.execute()

    assert len(result) == 6

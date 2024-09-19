from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .application.get_all_brands_use_case import GetAllBrandsUseCase
from .application.get_all_models_use_case import GetAllModelsUseCase
from .application.get_models_by_brand_id_use_case import GetModelsByBrandIdUseCase
from .application.insert_brand_use_case import InsertBrandUseCase
from .application.insert_model_use_case import InsertModelUseCase
from .application.update_average_price_by_model_id_use_case import UpdateAveragePriceByModelId
from .infrastructure.json_brands_repository import JSONBrandsRepository
from .infrastructure.json_greater_than_criteria import JSONGreaterThanCriteria
from .infrastructure.json_less_than_criteria import JSONLessThanCriteria
from .infrastructure.json_models_repository import JSONModelsRepository


models_repository=JSONModelsRepository()
brands_repository=JSONBrandsRepository()

class BrandList(APIView):
    def get(self, request):
        use_case = GetAllBrandsUseCase(brands_repository=brands_repository)
        result = use_case.execute()
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            name = request.data.get('name')
            use_case = InsertBrandUseCase(brands_repository=brands_repository)
            result = use_case.execute(name=name)
            return Response(result, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_409_CONFLICT)

class BrandModelsList(APIView):
    def get(self, request, brand_id):
        try:
            use_case = GetModelsByBrandIdUseCase(models_repository=models_repository, brands_repository=brands_repository)
            result = use_case.execute(brand_id=brand_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def post(self, request, brand_id):
        try:
            name = request.data.get('name')
            average_price = request.data.get('average_price')
            use_case = InsertModelUseCase(models_repository=models_repository, brands_repository=brands_repository)
            use_case.execute(brand_id=brand_id, name=name, average_price=average_price)
            return Response(None, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_409_CONFLICT)

class ModelList(APIView):
    def get(self, request):
        greater = request.query_params.get('greater')
        lower = request.query_params.get('lower')

        greater = int(greater) if greater is not None else None
        lower = int(lower) if lower is not None else None
        use_case = GetAllModelsUseCase(models_repository=models_repository, greater_than_criteria=JSONGreaterThanCriteria(min_price=greater), less_than_criteria=JSONLessThanCriteria(max_price=lower))
        result = use_case.execute(greater=greater, lower=lower)
        return Response(result, status=status.HTTP_200_OK)

class ModelDetail(APIView):
    def put(self, request, model_id):
        try:
            average_price = request.data.get('average_price')
            use_case = UpdateAveragePriceByModelId(models_repository=models_repository)
            use_case.execute(model_id=model_id, average_price=average_price)
            return Response(None, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_409_CONFLICT)
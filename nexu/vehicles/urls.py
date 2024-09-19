from django.urls import path
from .views import BrandList, BrandModelsList, ModelList, ModelDetail


urlpatterns = [
    path('brands/', BrandList.as_view(), name='brand-list'),
    path('brands/<int:brand_id>/models/', BrandModelsList.as_view(), name='brand-models'),
    path('models/', ModelList.as_view(), name='model-list'),
    path('models/<int:model_id>/', ModelDetail.as_view(), name='model-detail'),
]
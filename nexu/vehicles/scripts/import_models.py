import json
import os

from django.db.models import Sum

from vehicles.models import ModelModel, BrandModel


def run():
    if os.path.exists("models.json"):
        with open("models.json", "r") as file:
            data = json.load(file)
            for model in data:
                try:
                    brand = BrandModel.objects.get(name=model["brand_name"])
                    ModelModel(
                        name=model["name"],
                        average_price=model["average_price"],
                        brand=brand,
                    ).save()
                except BrandModel.DoesNotExist:
                    brand = BrandModel(name=model["brand_name"], average_price=0)
                    brand.save()
                    ModelModel(
                        name=model["name"],
                        average_price=model["average_price"],
                        brand=brand,
                    ).save()

            brands = BrandModel.objects.all()

            for brand in brands:
                total_average_price = ModelModel.objects.filter(brand=brand).aggregate(
                    Sum("average_price")
                )
                count_model = len(ModelModel.objects.filter(brand=brand))

                brand.average_price = (
                    total_average_price["average_price__sum"] / count_model
                )

                brand.save()

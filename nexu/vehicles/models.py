from django.db import models


class BrandModel(models.Model):
    name = models.CharField(max_length=255)
    average_price = models.IntegerField()


class ModelModel(models.Model):
    name = models.CharField(max_length=255)
    average_price = models.IntegerField()
    brand = models.ForeignKey("BrandModel", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

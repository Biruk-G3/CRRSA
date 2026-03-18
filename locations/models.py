from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCity(models.Model):
    name = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Woreda(models.Model):
    name = models.CharField(max_length=255)
    sub_city = models.ForeignKey(SubCity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.sub_city.name})"

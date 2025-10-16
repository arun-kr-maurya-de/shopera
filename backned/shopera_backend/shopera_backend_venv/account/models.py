from django.db import models

class Produc(models.Model):
    name = models.CharField(max_length=200)

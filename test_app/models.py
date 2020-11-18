from django.db import models

from bit_field.models import BitcoinField


class TestModel(models.Model):
    wallet = BitcoinField()

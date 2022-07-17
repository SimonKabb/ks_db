from django.db import models


class Ks_db(models.Model):
    id = models.PositiveIntegerField(primary_key=True, default='uuid.uuid4')
    ord = models.PositiveIntegerField()
    price = models.FloatField()
    rub = models.FloatField()
    delivery_time = models.DateField(auto_now_add=False)

    class Meta:
        db_table = 'ks_db'

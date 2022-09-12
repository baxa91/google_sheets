from django.db import models


class GoogleSheets(models.Model):
    number = models.BigIntegerField(primary_key=True, unique=True, verbose_name="№")
    order_number = models.CharField(
        max_length=200, null=True, blank=False,
        verbose_name="заказ №")
    price = models.CharField(
        max_length=200, null=True, blank=False,
        verbose_name="стоимость,$")
    price_rubles = models.CharField(
        max_length=200, null=True, blank=False,
        verbose_name="стоимость в рублях")
    date = models.DateField(null=True, blank=False, verbose_name="срок поставки")

from django.db import models


class GoogleSheets(models.Model):
    order_number = models.CharField(
        max_length=200, null=False, blank=False,
        verbose_name="заказ №")
    price = models.CharField(
        max_length=200, null=False, blank=False,
        verbose_name="стоимость,$")
    date = models.DateField(null=False, blank=False, verbose_name="срок поставки")

# Generated by Django 4.1.1 on 2022-09-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_sheets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googlesheets',
            name='id',
        ),
        migrations.AddField(
            model_name='googlesheets',
            name='number',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False, unique=True, verbose_name='№'),
        ),
        migrations.AddField(
            model_name='googlesheets',
            name='price_rubles',
            field=models.CharField(max_length=200, null=True, verbose_name='стоимость в рублях'),
        ),
        migrations.AlterField(
            model_name='googlesheets',
            name='date',
            field=models.DateField(null=True, verbose_name='срок поставки'),
        ),
        migrations.AlterField(
            model_name='googlesheets',
            name='order_number',
            field=models.CharField(max_length=200, null=True, verbose_name='заказ №'),
        ),
        migrations.AlterField(
            model_name='googlesheets',
            name='price',
            field=models.CharField(max_length=200, null=True, verbose_name='стоимость,$'),
        ),
    ]

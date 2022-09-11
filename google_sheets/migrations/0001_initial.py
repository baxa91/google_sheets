# Generated by Django 4.1.1 on 2022-09-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleSheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=200, verbose_name='заказ №')),
                ('price', models.CharField(max_length=200, verbose_name='стоимость,$')),
                ('date', models.DateField(verbose_name='срок поставки')),
            ],
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190922_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20190922_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(max_length=120),
        ),
    ]
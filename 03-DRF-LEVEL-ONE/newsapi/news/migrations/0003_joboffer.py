# Generated by Django 2.2.5 on 2019-09-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190919_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('company_email', models.CharField(max_length=120)),
                ('job_title', models.CharField(max_length=120)),
                ('salary', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
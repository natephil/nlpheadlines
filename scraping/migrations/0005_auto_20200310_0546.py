# Generated by Django 3.0.3 on 2020-03-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20200310_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]

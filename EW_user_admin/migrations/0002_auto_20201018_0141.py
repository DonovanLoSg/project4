# Generated by Django 2.2.13 on 2020-10-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EW_user_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
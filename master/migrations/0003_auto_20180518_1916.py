# Generated by Django 2.0.5 on 2018-05-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20180518_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productBrand',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productId',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(null=True),
        ),
    ]
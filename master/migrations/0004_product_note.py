# Generated by Django 2.0.5 on 2018-06-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20180604_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
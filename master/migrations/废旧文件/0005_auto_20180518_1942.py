# Generated by Django 2.0.5 on 2018-05-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20180518_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]

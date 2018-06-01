# Generated by Django 2.0.5 on 2018-05-24 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BomItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCount', models.FloatField()),
                ('note', models.TextField(null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyPhone', models.CharField(max_length=20, null=True)),
                ('companyAddress', models.CharField(max_length=200, null=True)),
                ('CompanyContactType', models.CharField(max_length=20, null=True)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Company')),
            ],
        ),
        migrations.CreateModel(
            name='partUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension', models.CharField(db_index=True, max_length=20, unique=True)),
                ('conversion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(db_index=True, max_length=20, unique=True)),
                ('productName', models.CharField(db_index=True, max_length=20, null=True)),
                ('specification', models.CharField(db_index=True, max_length=200, null=True)),
                ('productBrand', models.CharField(db_index=True, max_length=20, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=20, null=True)),
                ('job', models.CharField(max_length=20, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Company')),
                ('userId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffPhone', models.CharField(max_length=20, null=True)),
                ('staffPhoneType', models.CharField(max_length=20, null=True)),
                ('staffId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='master.Tag'),
        ),
        migrations.AddField(
            model_name='bomitem',
            name='parentProduct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bom', to='master.Product'),
        ),
        migrations.AddField(
            model_name='bomitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Product'),
        ),
        migrations.AddField(
            model_name='bomitem',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.partUnit'),
        ),
    ]

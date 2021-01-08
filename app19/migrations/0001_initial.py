# Generated by Django 3.0.1 on 2020-05-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='product_images/')),
                ('pdate', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerveceria', '0006_marca_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
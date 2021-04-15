# Generated by Django 3.1.7 on 2021-03-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='capturas')),
                ('tipo', models.CharField(max_length=60)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cerveceria.marca')),
            ],
        ),
    ]
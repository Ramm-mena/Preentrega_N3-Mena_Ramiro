# Generated by Django 4.2.3 on 2023-07-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_n3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Gerente',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]

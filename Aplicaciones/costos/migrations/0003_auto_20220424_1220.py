# Generated by Django 2.2.3 on 2022-04-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0002_auto_20220423_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientesreceta',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='ingredientesreceta',
            name='ingredientes',
            field=models.ManyToManyField(to='costos.Ingredientes'),
        ),
    ]
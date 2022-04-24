# Generated by Django 2.2.3 on 2022-04-24 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0003_auto_20220424_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientesreceta',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='receta',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, through='costos.IngredientesReceta', to='costos.Ingredientes'),
        ),
        migrations.RemoveField(
            model_name='ingredientesreceta',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='ingredientesreceta',
            name='ingredientes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='costos.Ingredientes'),
        ),
        migrations.AlterField(
            model_name='ingredientesreceta',
            name='receta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='costos.Receta'),
        ),
        migrations.AlterField(
            model_name='ingredientesreceta',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]

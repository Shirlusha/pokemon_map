# Generated by Django 3.1.8 on 2021-04-21 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20210421_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity', to='pokemon_entities.pokemon', verbose_name='покемон'),
        ),
    ]
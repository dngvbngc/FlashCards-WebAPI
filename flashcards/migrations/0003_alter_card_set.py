# Generated by Django 4.2.7 on 2024-01-06 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("flashcards", "0002_set_card"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="set",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cards",
                to="flashcards.set",
            ),
        ),
    ]

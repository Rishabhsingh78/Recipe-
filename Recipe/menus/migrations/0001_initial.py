# Generated by Django 4.2.1 on 2023-05-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("descriptions", models.TextField()),
                ("ingredients", models.TextField()),
                ("instructions", models.TextField()),
                ("prep_time", models.PositiveIntegerField()),
                ("cook_time", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

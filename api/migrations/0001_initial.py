# Generated by Django 4.2.10 on 2024-02-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("implementation", models.CharField(default="", max_length=255)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("deleedAt", models.DateTimeField(default=None)),
            ],
        ),
    ]

# Generated by Django 4.2.10 on 2024-05-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_remove_testexecution_referenceid_test_referenceid"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="executions",
            field=models.IntegerField(default=0),
        ),
    ]

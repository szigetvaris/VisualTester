# Generated by Django 4.2.10 on 2024-05-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_alter_testexecution_testplanexecutionid"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimage",
            name="status",
            field=models.CharField(
                choices=[("Pass", "Pass"), ("Fail", "Fail"), ("TODO", "TODO")],
                default="TODO",
                max_length=20,
            ),
        ),
    ]

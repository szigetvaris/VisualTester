# Generated by Django 4.2.10 on 2024-04-29 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_testplan_runat"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestExecution",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pass", "Pass"),
                            ("Fail", "Fail"),
                            ("Not Run", "Not Run"),
                        ],
                        default="Not Run",
                        max_length=20,
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("bugs", models.IntegerField(null=True)),
                ("executionTime", models.FloatField(null=True)),
                ("referenceID", models.IntegerField(default=True)),
                ("info", models.CharField(max_length=511, null=True)),
                (
                    "testID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.test"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TestPlanExecution",
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
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Not Started", "Not Started"),
                            ("In Progress", "In Progress"),
                            ("Completed", "Completed"),
                        ],
                        default="Not Started",
                        max_length=20,
                    ),
                ),
                (
                    "testPlanID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.testplan"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TestImage",
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
                ("name", models.CharField(max_length=127)),
                ("imagePath", models.CharField(max_length=255)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "testExecutionID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.testexecution",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="testexecution",
            name="testPlanExecutionID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.testplanexecution"
            ),
        ),
    ]

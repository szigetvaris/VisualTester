from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255, null=True)
    testType = models.CharField(max_length=255, null=True)
    implementation = models.CharField(max_length=255, default='')
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True)


class TestPlan(models.Model):
    name = models.CharField(max_length=255)
    runAt = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True)


class Contains(models.Model):
    testID = models.ForeignKey(Test, models.CASCADE)
    testPlanID = models.ForeignKey(TestPlan, models.CASCADE)

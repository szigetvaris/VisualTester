from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=255, null=True)
    testType = models.CharField(max_length=255, null=True)
    implementation = models.CharField(max_length=255, default='')
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True)



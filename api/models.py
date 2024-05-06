from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255, null=True)
    testType = models.CharField(max_length=255, null=True)
    implementation = models.CharField(max_length=255, default='')
    referenceID = models.IntegerField(null=True) # ID of the pervious successful execution
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True)
    executions = models.IntegerField(default=0)


class TestPlan(models.Model):
    name = models.CharField(max_length=255)
    runAt = models.CharField(max_length=255, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True)


class Contains(models.Model):
    testID = models.ForeignKey(Test, models.CASCADE)
    testPlanID = models.ForeignKey(TestPlan, models.CASCADE)

class TestPlanExecution(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    testPlanID = models.ForeignKey(TestPlan, models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    
class TestExecution(models.Model):
    STATUS_CHOICES = [
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('Not Run', 'Not Run'),
    ]
    
    testID = models.ForeignKey(Test, models.CASCADE)
    testPlanExecutionID = models.ForeignKey(TestPlanExecution, models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Run')
    createdAt = models.DateTimeField(auto_now_add=True)
    bugs = models.IntegerField(default=0) # Number of different images
    executionTime = models.FloatField(null=True) # Time from cypress logs
    info = models.CharField(max_length=511, null=True) # Info extracted from cypress logs
    
class TestImage(models.Model):
    STATUS_CHOICES = [
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('TODO', 'TODO'),
    ]
    
    testExecutionID = models.ForeignKey(TestExecution, models.CASCADE)
    name = models.CharField(max_length=127)
    imagePath = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    
    
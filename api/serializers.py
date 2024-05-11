from rest_framework import serializers
from .models import Test, TestPlan, TestExecution, TestPlanExecution


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'testType',
                  'implementation', 'createdAt', 'deletedAt')


class CreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        # only fields we want to declare.. fucking important comma if there is only one field -_-
        fields = ('name', 'testType', 'implementation')


class TestPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlan
        fields = ('id', 'name', 'runAt', 'createdAt', 'deletedAt')


class CreateTestPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlan
        fields = ('name',)


class TestExecutionSerializer(serializers.ModelSerializer):
    testID = serializers.PrimaryKeyRelatedField(read_only=True)
    testPlanExecutionID = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TestExecution
        fields = ['id', 'testID', 'testPlanExecutionID', 'status',
                  'createdAt', 'bugs', 'executionTime', 'info']

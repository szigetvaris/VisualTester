from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'implementation', 'createdAt', 'deletedAt')


class CreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        # only fields we want to declare.. fucking important comma if there is only one field -_-
        fields = ('implementation', )
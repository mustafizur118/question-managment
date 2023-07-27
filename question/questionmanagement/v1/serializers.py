from rest_framework import serializers
from question.questionmanagement.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserCountSerializer:
    pass

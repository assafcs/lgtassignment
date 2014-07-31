from question_table.models import Question
from rest_framework.serializers import ModelSerializer

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'description')

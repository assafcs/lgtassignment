from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from question_table.models import Question
from question_table.serializers import QuestionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializers = QuestionSerializer(questions)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):
    q = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        serializer = QuestionSerializer(q)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(q, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def questions_view(request):
    return render(request, 'question_table/index.html', {})

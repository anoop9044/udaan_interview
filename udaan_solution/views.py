from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from udaan_solution.models import Quiz
from udaan_solution.serializer import QuestionSerializer, QuizSerializer, AnswerChoiceSerializer, ResponseSerializer
from django.core.paginator import Paginator


# Create your views here.

class QuizView(APIView):
    def post(self, request):
        quiz_name = request.data.get("quiz_name")
        if not quiz_name:
            return HttpResponse(status=400)
        serialized = QuizSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

    def get(self, request):
        try:
            page_number = request.data.get("page_number", 1)
            page_size = request.data.get("page_size", 10)
            if not page_number:
                return HttpResponse(status=400)
            quiz_qs = Quiz.objects.all()
            quiz_page_qs = Paginator(quiz_qs, page_size)
            quize_on_page = quiz_page_qs.page(page_number)
            quiz_list = []
            for quiz in quize_on_page:
                quiz_list.append(quiz.quiz_name)
            return JsonResponse(status=200, data={"quiz": quiz_list}, safe=False)
        except:
            return JsonResponse(status=500, data="Something went wrong")


class QuestionView(APIView):
    def post(self, request):
        question = request.data.get("question_description")
        quizes = request.data.get("quiz")
        if not quizes or not question:
            print("bad")
            return HttpResponse(status=400)
        serialized = QuestionSerializer(data={"question_description": question, "quiz": quizes})
        if serialized.is_valid():
            serialized.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


class AnswerView(APIView):
    def post(self, request):
        serialized = AnswerChoiceSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


class QuizResponseView(APIView):
    def post(self, request):
        try:
            serialized = ResponseSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        except:
            return JsonResponse(status=400, data="Something went Wrong", safe=False)

from django.contrib import admin
from udaan_solution.models import Quiz, Question, AnswerChoice, Response


# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(AnswerChoice)
class AnswerChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    pass
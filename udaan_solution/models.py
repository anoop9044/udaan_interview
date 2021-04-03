from django.db import models


# Create your models here.

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200, null=False, blank=False)
    quiz_description = models.CharField(max_length=500, null=True, blank=True)



class Question(models.Model):
    quiz = models.ManyToManyField(Quiz, null=False, blank=False)
    question_description = models.CharField(max_length=2000, null=False, blank=False)



class AnswerChoice(models.Model):
    choice = models.CharField(null=False, blank=False, max_length=100)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)


class Response(models.Model):
    choice = models.ForeignKey(AnswerChoice, null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)

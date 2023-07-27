from django.db import models


class User(models.Model):
    id = models.CharField(max_length=250, unique=True)
    display_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)


class Question(models.Model):
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    option5 = models.TextField()
    answer = models.IntegerField()
    explain = models.TextField()


class FavoriteQuestion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


class ReadQuestion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

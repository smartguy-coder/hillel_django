from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_poll = models.DateTimeField('date published', auto_now_add=True)
    opened = models.BooleanField(default=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=5)

    def __str__(self):
        return self.question_text

    class Meta:
        # old first
        ordering = ['time_poll',]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_time = models.DateTimeField('date published', auto_now_add=True)
    votes = models.IntegerField(default=0)

    class Meta:
        # new first
        ordering = ['-choice_time',]

    def __str__(self):
        return self.choice_text


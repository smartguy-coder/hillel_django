from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_poll = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('date published')

from django.urls import path


from .views import *

urlpatterns = [
    path('', index_view, name='questions'),
    path('answers/', answers_view, name='answers'),
    path('new_question/', add_question, name='new_question'),
    path('new_answer/', add_answer, name='new_answer'),
    path('detail/<int:pk>', QuestionAndAllAnswers.as_view(), name='question_details')
    ]
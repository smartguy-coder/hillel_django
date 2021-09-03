from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .forms import *
from .models import Choice, Question
from django.db.models import Count


def index_view(request):

    # new first
    questions = Question.objects.all().order_by('-time_poll')

    return render(request, 'poll/index.html', context={"questions": questions})


class QuestionAndAllAnswers(DetailView):
    model = Question
    template_name = 'poll/detail-view.html'
    context_object_name = 'detail'




def answers_view(request):
    answers = Choice.objects.all()
    return render(request, 'poll/answers.html', context={"answers": answers})


def add_question(request):
    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            try:
                Question.objects.create(**form.cleaned_data)
                return redirect('questions')
            except:
                form.add_error(None, "There was a problem with adding a new question")
    else:
        form = NewQuestion()

    return render(request, 'poll/addquestion.html', context={'form': form})


def add_answer(request):

    if request.method == 'POST':
        form = NewChoice(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Choice.objects.create(**form.cleaned_data)
                return redirect('answers')
            except:
                form.add_error(None, "There was a problem with adding a new question")
    else:
        form = NewChoice()

    return render(request, 'poll/addchoice.html', context={'form': form})


import logging

from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice

logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):  # 최근 생성된 질문 5 개를 반환
        return Question.objects.all().order_by("-pub_date")[:5]
        # return Question.objects.order_by("-pub_date")[:5] # all() 은 생략되어 있어서 그냥써도 똑같음


# Create your views here.
def index(request): # class IndexView(generic.ListView): 와 같은 내용!
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, "value": "Hello,\nWorld!",
               "value2": "동해물과 백두산이 마르고 닳도록",
               "value3": [1, 2, 3],
               "value4": False,
               "value5": "<strong>Hello, World!</strong>"}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    logger.debug("vote")
    logger.fatal("vote")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

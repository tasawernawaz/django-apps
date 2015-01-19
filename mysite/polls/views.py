from django.core.urlresolvers import reverse

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        return Question.objects.order_by('-id')


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

#
#
# def index(request):
#     latest_questions = Question.objects.order_by('-id')
#     # template = loader.get_template("polls/index.html")
#     # context = RequestContext(request, {"latest_questions" : latest_questions,})
#     # return HttpResponse(template.render(context))
#
#     return render(request, "polls/index.html", {"latest_questions": latest_questions})

#
# def detail(request, question_id):
#     try:
#         # question = Question.objects.get(pk=question_id)
#         question = get_object_or_404(Question, pk=question_id)
#     except:
#         raise Http404
#         # return render(request, "polls/detail.html", {"question" : question})
#
#     return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


def votes(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, "polls/detail.html",
                      {"question": q, "error_message": "Please select an option before submitting"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(q.id,)))



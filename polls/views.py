from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import Question,Choice
from django.views.generic import ListView,DetailView
from django.utils import timezone
# Create your views here.

class HomeView(ListView):
    template_name="polls/home.html"
    context_object_name="latest_question_list"
    def get_queryset(self):
        return Question.objects.filter(publication_date__lte=timezone.now()).order_by("-publication_date")[:5]
    

class DetailView(DetailView):
    model=Question
    template_name="polls/detail.html"
    

class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,
                                                   "error_message":"You didnt select a choice"})
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))
    
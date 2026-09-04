from django.shortcuts import render,get_object_or_404

from .models import Question
# Create your views here.

def home(request):
    latest_question_list=Question.objects.order_by("-publication_date")[:5]
    return render(request,"polls/home.html",{"latest_question_list":latest_question_list})

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request,question_id):
    return HttpResponse(f"You are voting on question {question_id}")
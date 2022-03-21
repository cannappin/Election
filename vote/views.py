
from django.shortcuts import get_object_or_404, render
from .models import Question, Serie, Realisateur, Genre, Plateform, Acteur
from django.http import  HttpResponseRedirect
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('date_question')[:5]
    context = {'question_list': latest_question_list}
    return render(request, 'vote/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)    
    return render(request, 'vote/detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote/results.html', {'question':question, })

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.serie_set.get(pk=request.POST['serie'])
    except (KeyError, Serie.DoesNotExist):
        return render(request, 'vote/detail.html', {'question':question, 'error_message': 'Vous devez choisir',})
    
    else:
        selected_choice.votes_serie += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('vote:results', args=(question_id,)))
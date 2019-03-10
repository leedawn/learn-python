from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from .models import Game,Result
from .forms import GameForm,ResultForm
import json
# Create your views here.
def index(request):
    return render(request,'game_results/index.html')

def games(request):
    games=Game.objects.order_by('date_added')
    context={'games':games}
    return render(request,'game_results/games.html',context)

def game(request,game_id):
    game=Game.objects.get(id=game_id)
    results=game.result_set.order_by('-date_added')
    context={'game':game,"results":results}
    return render(request,'game_results/game.html',context)

def new_game(request):
    if request.method!='POST':
        form=GameForm()
    else:
        form=GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('game_results:games'))

    context={'form':form}
    return render(request,'game_results/new_game.html',context)

def new_result(request,game_id):
    game=Game.objects.get(id=game_id)
    if request.method != 'POST':
        form=ResultForm()
    else:
        form=ResultForm(data=request.POST)
        if form.is_valid():
            new_result=form.save(commit=False)
            new_result.game=game
            new_result.save()
            return HttpResponseRedirect(reverse('game_results:game',
                                                args=[game_id]))

    context={'game':game,'form':form}
    return render(request,'game_results/new_result.html',context)

def edit_result(request,result_id):
    result=Result.objects.get(id=result_id)
    game=result.game

    if request.method!='POST':
        form=ResultForm(instance=result)
    else:
        form=ResultForm(instance=result,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('game_results:game',
                                                args=[game.id]))

    context={'result':result,'game':game,'form':form}
    return render(request,'game_results/edit_result.html',context)

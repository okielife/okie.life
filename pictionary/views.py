import json
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from pictionary.models import WordModel


def home(request):
    return render(request, 'pictionary/home.html')


def player(request):
    return render(request, 'pictionary/player.html')


def audience(request):
    return render(request, 'pictionary/audience.html')


def up_vote(request):
    data = json.loads(request.body)
    word = WordModel.objects.get(pk=data['pk'])
    word.up_votes += 1
    word.save()
    return HttpResponse()


def down_vote(request):
    data = json.loads(request.body)
    word = WordModel.objects.get(pk=data['pk'])
    word.down_votes += 1
    word.save()
    return HttpResponse()


def get_word(request):
    if WordModel.objects.count() == 0:
        word = {'word': 'Initialize Database'}
    else:
        random_idx = random.randint(0, WordModel.objects.count() - 1)
        word_model = WordModel.objects.all()[random_idx]
        word = {'id': word_model.id, 'word': word_model.word}
    return JsonResponse({'word': word})

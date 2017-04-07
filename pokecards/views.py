from django.shortcuts import render
from django.views import generic
from .models import CardInstance, Card, GameState
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from random import shuffle


def index(request):
    return render(request, 'pokecards/index.html')


class MyCardInstancesListView(LoginRequiredMixin, generic.ListView):
    model = CardInstance
    template_name = 'pokecards/my_cards.html'
    paginate_by = 5

    def get_queryset(self):
        return CardInstance.objects.filter(owner=self.request.user)


class CardInstanceDetailView(generic.DetailView):
    model = CardInstance
    template_name = 'pokecards/instance_detail_view.html'


class AllCardsView(generic.ListView):
    model = Card
    template_name = 'pokecards/all_cards.html'
    paginate_by = 5

    def get_queryset(self):
        return Card.objects.order_by('character')


class CardDetailView(generic.DetailView):
    model = Card
    template_name = 'pokecards/detail_view.html'


@login_required
def create_card(request):
    if not request.method == "POST":
        return JsonResponse({'message': u"Only accepts POST requests"}, status=405)
    post = request.POST.copy()
    if 'character' in post and 'image_path' in post:
        if Card.objects.filter(character=post['character']).count() > 0:
            return JsonResponse({'message': u"Character name already in use."}, status=400)
        new_char = Card.objects.create(character=post['character'], static_image_path=post['image_path'])
        return HttpResponseRedirect(reverse('pokecards:card-detail', args=[new_char.id]))
    else:
        return JsonResponse({'message': u"Insufficient POST data (need 'character' and 'image_path')"}, status=400)


@login_required
def ajax_create_card(request):
    if not request.method == "POST":
        return JsonResponse({'message': u"Only accepts POST requests"}, status=405)
    post = request.POST.copy()
    if 'character' in post and 'image_path' in post:
        if Card.objects.filter(character=post['character']).count() > 0:
            return JsonResponse({'message': u"Character name already in use."}, status=400)
        else:
            Card.objects.create(character=post['character'], static_image_path=post['image_path'])
            return JsonResponse({'character': post['character'], 'image_path': post['image_path']})
    else:
        return JsonResponse({'msg': u"Requires both 'slug' and 'title'!"}, status=400)


@login_required
def ajax_create_game(request):
    this_user = User.objects.get(id=request.user.id)
    users_games = GameState.objects.filter(player=this_user)
    if not request.method == "POST":
        return JsonResponse({'message': u"Only accepts POST requests"}, status=405)
    post = request.POST.copy()
    if 'nickname' in post:
        if users_games.filter(game_nickname=post['nickname']).count() > 0:
            return JsonResponse({'message': u"Game name name already in use."}, status=400)
        else:
            g = GameState.objects.create(game_nickname=post['nickname'], player=this_user)
            return JsonResponse({'nickname': post['nickname'], 'id': g.pk})
    else:
        return JsonResponse({'msg': u"Requires a 'nickname'!"}, status=400)


def ajax_char_available(request):
    if not request.method == 'GET':
        return JsonResponse({'message': u"Only accepts GET requests"}, status=405)
    if 'character' in request.GET:
        if Card.objects.filter(character=request.GET['character']).count() == 0:
            return JsonResponse(data={'available': 'true'})
        else:
            return JsonResponse(data={'available': 'false'})


class GameListView(generic.ListView):
    model = GameState
    template_name = 'pokecards/game/list_my_games.html'

    def get_queryset(self):
        return GameState.objects.filter(player=self.request.user)


def game_continue(request, pk):
    try:
        current_game = GameState.objects.get(id=pk)
    except GameState.DoesNotExist:
        return JsonResponse({'error':'Game state with pk = {0} does not exist'.format(pk)}, status=404)
    incorrect_answers = ["Foo", "Bar", "Joe"]  # TODO: get this from current game level
    correct_answer = ["OK"]  # TODO: get this from current game level
    answers_list = incorrect_answers + correct_answer
    shuffle(answers_list)
    return render(request, 'pokecards/game/continue_game.html', context={'game': current_game, 'answers': answers_list})


def game_answer(request, pk):
    try:
        current_game = GameState.objects.get(id=pk)
    except GameState.DoesNotExist:
        return JsonResponse({'error': 'Game state with pk = {0} does not exist'.format(pk)}, status=404)
    if not request.method == "POST":
        return JsonResponse({'message': u"Only accepts POST requests"}, status=405)
    post = request.POST.copy()
    correct_answer = "OK"  # TODO: get this from current game level
    if not 'answer' in post:
        return JsonResponse({'error': 'Could not find an answer in the submission, try again'}, status=400)
    if post['answer'] == correct_answer:
        current_game.level += 1
        current_game.save()
        return render(request,
                      'pokecards/game/question_answered.html',
                      context={'game': current_game,
                               'announcement': "Hooray!",
                               'second_heading': "Correct Answer",
                               'continue_word': "Continue Game"})
    else:
        return render(request,
                      'pokecards/game/question_answered.html',
                      context={'game': current_game,
                               'announcement': "Oops!",
                               'second_heading': "Incorrect Answer",
                               'continue_word': "Try Again!"})


def game_start(request):
    return render(request, 'pokecards/game/start_new_game.html')


def delete_game(request, pk):
    try:
        current_game = GameState.objects.get(id=pk)
    except GameState.DoesNotExist:
        return JsonResponse({'error': 'Game state with pk = {0} does not exist'.format(pk)}, status=404)
    return render(request, 'pokecards/game/delete_game.html', context={'game': current_game})


def ajax_delete_game(request, pk):
    this_user = User.objects.get(id=request.user.id)
    users_games = GameState.objects.filter(player=this_user)
    try:
        game_to_delete = users_games.filter(id=pk)
    except GameState.DoesNotExist:
        return JsonResponse({'error': 'Game did not appear to belong to this user'}, status=400)
    if not request.method == "POST":  # should be delete, but ajax isn't liking it...
        return JsonResponse({'message': u"Only accepts POST requests"}, status=405)
    try:
        game_to_delete.delete()
    except:  # what exceptions would I catch?
        return JsonResponse({'message': u"Could not delete...weird"}, status=405)
    return JsonResponse({'message': 'success'})

from django.shortcuts import render
from django.views import generic
from .models import CardInstance, Card
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


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
        return HttpResponseRedirect(reverse('card-detail', args=[new_char.id]))
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


def ajax_char_available(request):
    if not request.method == 'GET':
        return JsonResponse({'message': u"Only accepts GET requests"}, status=405)
    if 'character' in request.GET:
        if Card.objects.filter(character=request.GET['character']).count() == 0:
            return JsonResponse(data={'available': 'true'})
        else:
            return JsonResponse(data={'available': 'false'})

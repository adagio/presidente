from django.shortcuts import render
from django.http import HttpResponse

from .models import Card, AttackCard, VotesCard


def index(request):
    latest_card_list = Card.objects.all()
    context = {
        'latest_card_list': latest_card_list,
    }
    return render(request, 'cards/index.html', context)


def cards_by_type(request):
    attack_card_list = AttackCard.objects.all()
    votes_card_list = VotesCard.objects.all()
    shield_card_list = Card.objects.filter(card_type__name__contains='blindaje')
    money_card_list = Card.objects.filter(card_type__name__contains='dinero')
    power_card_list = Card.objects.filter(card_type__name__contains='poder')
    context = {
        'attack_card_list': attack_card_list,
        'votes_card_list': votes_card_list,
        'shield_card_list': shield_card_list,
        'money_card_list': money_card_list,
        'power_card_list': power_card_list
    }
    return render(request, 'cards/by-type.html', context)


def detail(request, id):
    card = Card.objects.get(pk=id)
    return render(request, 'cards/detail.html', {'card': card})



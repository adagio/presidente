from django.contrib import admin

from .models import Card, VotesCard, CardType

admin.site.register(Card)
admin.site.register(VotesCard)
admin.site.register(CardType)

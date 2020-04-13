from django.contrib import admin

from .models import Card, VotesCard, AttackCard, CardType

admin.site.register(Card)
admin.site.register(VotesCard)
admin.site.register(AttackCard)
admin.site.register(CardType)

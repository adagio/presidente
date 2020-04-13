from django.db import models

class CardType(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Card(models.Model):
    text = models.TextField(max_length=60)
    card_type = models.ForeignKey(
        CardType,
        related_name='related_primary_card_type',
        verbose_name="Card Type",
        on_delete=models.CASCADE
    )
    requirements = models.ForeignKey(
        CardType,
        related_name='related_secondary_card_type',
        verbose_name="Requirements",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_corrupt = models.BooleanField(default=False)
    def __str__(self):
        return self.text


class VotesCard(Card):
    votes = models.IntegerField()


class AttackCard(Card):
    only_attacks_corrupt = models.BooleanField(default=False)


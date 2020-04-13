from django.db import models

class CardType(models.Model):
    name = models.CharField(max_length=10)
    emoji = models.CharField(max_length=2, blank=True, null=True,)
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
    requirements = models.ManyToManyField(
        CardType,
        related_name='related_secondary_card_type',
        verbose_name="Requirements",
        blank=True,
        null=True,
    )
    is_corrupt = models.BooleanField(default=False)
    def __str__(self):
        return self.text


DEFAULT_ATTACK_TYPE_ID = 3
class VotesCard(Card):
    votes = models.IntegerField()


DEFAULT_ATTACK_TYPE_ID = 1
class AttackCard(Card):
    only_attacks_corrupt = models.BooleanField(default=False)
    attack_type = models.ForeignKey(
        CardType,
        related_name='related_card_attack_type',
        verbose_name="Card Attack Type",
        on_delete=models.CASCADE,
        default=DEFAULT_ATTACK_TYPE_ID
    )

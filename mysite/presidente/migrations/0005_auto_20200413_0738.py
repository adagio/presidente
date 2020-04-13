# Generated by Django 3.0.5 on 2020-04-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presidente', '0004_auto_20200413_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='requirements',
        ),
        migrations.AddField(
            model_name='card',
            name='requirements',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_secondary_card_type', to='presidente.CardType', verbose_name='Requirements'),
        ),
    ]
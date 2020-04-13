# Generated by Django 3.0.5 on 2020-04-13 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presidente', '0003_auto_20200413_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='only_attacks_corrupt',
        ),
        migrations.CreateModel(
            name='AttackCard',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='presidente.Card')),
                ('only_attacks_corrupt', models.BooleanField(default=False)),
            ],
            bases=('presidente.card',),
        ),
        migrations.CreateModel(
            name='VotesCard',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='presidente.Card')),
                ('votes', models.IntegerField()),
            ],
            bases=('presidente.card',),
        ),
    ]

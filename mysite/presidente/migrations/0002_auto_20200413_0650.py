# Generated by Django 3.0.5 on 2020-04-13 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presidente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='requirements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_secondary_card_type', to='presidente.CardType', verbose_name='Requirements'),
        ),
    ]

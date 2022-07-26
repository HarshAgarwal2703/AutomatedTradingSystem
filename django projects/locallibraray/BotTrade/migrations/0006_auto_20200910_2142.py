# Generated by Django 2.2.1 on 2020-09-10 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BotTrade', '0005_auto_20200910_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='orderHistory',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='orderhistorydb',
            name='userId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='BotTrade.UserDb'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliodb',
            name='userId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='BotTrade.UserDb'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlistdb',
            name='userId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='BotTrade.UserDb'),
            preserve_default=False,
        ),
    ]

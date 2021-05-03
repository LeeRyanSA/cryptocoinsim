# Generated by Django 2.1 on 2018-08-24 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0003_auto_20180824_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='user_name',
        ),
        migrations.AddField(
            model_name='balance',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

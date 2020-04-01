# Generated by Django 2.2 on 2020-04-01 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0004_remove_link_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='who has created the link?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]

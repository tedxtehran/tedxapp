# Generated by Django 2.2 on 2020-04-01 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_remove_speaker_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['session', 'ordering', 'start_time', 'title'], 'verbose_name': 'talk', 'verbose_name_plural': 'talks'},
        ),
    ]

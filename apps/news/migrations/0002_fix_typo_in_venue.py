# Generated by Django 2.2 on 2020-10-01 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['organizer', 'title'], 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]

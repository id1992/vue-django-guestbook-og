# Generated by Django 2.0.7 on 2018-07-30 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestbook',
            old_name='article_id',
            new_name='guestbook_id',
        ),
        migrations.RenameField(
            model_name='guestbook',
            old_name='article_name',
            new_name='guestbook_name',
        ),
        migrations.RenameField(
            model_name='guestbook',
            old_name='article_context',
            new_name='guestbook_text',
        ),
    ]
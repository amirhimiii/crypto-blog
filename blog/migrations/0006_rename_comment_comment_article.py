# Generated by Django 4.1 on 2022-09-08 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articlehit_article_hits_articlehit_article_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='article',
        ),
    ]

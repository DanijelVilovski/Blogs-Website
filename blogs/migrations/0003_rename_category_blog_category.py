# Generated by Django 4.1.1 on 2022-10-10 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_category_blog_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Category',
            new_name='category',
        ),
    ]

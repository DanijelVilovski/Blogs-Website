# Generated by Django 4.1.1 on 2022-10-17 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
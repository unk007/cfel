# Generated by Django 4.0.4 on 2022-05-09 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paids', '0007_rename_what_money_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='fuller',
        ),
    ]

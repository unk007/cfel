# Generated by Django 4.0.4 on 2022-04-23 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paids', '0002_alter_table_payer_id_alter_table_taker_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='payer_id',
            new_name='payer',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='taker_id',
            new_name='taker',
        ),
    ]

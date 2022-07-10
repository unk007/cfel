# Generated by Django 4.0.2 on 2022-03-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('cash', models.BigIntegerField()),
                ('payer_id', models.BigIntegerField()),
                ('taker_id', models.BigIntegerField()),
                ('diliver_paid', models.BigIntegerField(null=True)),
                ('sanction', models.BooleanField(null=True)),
                ('sanction_date', models.CharField(max_length=255, null=True)),
                ('payer_comment', models.CharField(max_length=255, null=True)),
                ('taker_comment', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
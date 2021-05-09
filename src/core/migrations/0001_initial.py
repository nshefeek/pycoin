# Generated by Django 3.2.2 on 2021-05-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(max_length=5)),
                ('to_currency', models.CharField(max_length=5)),
                ('exchange', models.FloatField()),
                ('last_refreshed', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
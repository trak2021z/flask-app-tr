# Generated by Django 2.2.5 on 2021-06-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0013_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='cumulative_deaths',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
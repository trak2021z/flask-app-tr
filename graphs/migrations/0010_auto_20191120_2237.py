# Generated by Django 2.2.7 on 2019-11-20 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0009_auto_20191120_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='graphs.RoomType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id_staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('<django.db.models.query_utils.DeferredAttribute object at 0x03CDF970> <django.db.models.query_utils.DeferredAttribute object at 0x03CDF990>'), related_name='id_staff', to=settings.AUTH_USER_MODEL),
        ),
    ]

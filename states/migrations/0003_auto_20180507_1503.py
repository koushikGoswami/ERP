# Generated by Django 2.0.3 on 2018-05-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_state_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='d_status',
        ),
        migrations.AddField(
            model_name='state',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
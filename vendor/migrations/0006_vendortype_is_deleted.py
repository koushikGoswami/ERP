# Generated by Django 2.0.3 on 2018-06-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_auto_20180531_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendortype',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

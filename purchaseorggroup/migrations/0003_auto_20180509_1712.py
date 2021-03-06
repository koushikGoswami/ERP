# Generated by Django 2.0.3 on 2018-05-09 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_branch', '0004_auto_20180508_1448'),
        ('purchaseorggroup', '0002_purchaseorgmapping'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchaseorgmapping',
            unique_together={('pur_org', 'branch')},
        ),
        migrations.AlterIndexTogether(
            name='purchaseorgmapping',
            index_together={('pur_org', 'branch')},
        ),
    ]

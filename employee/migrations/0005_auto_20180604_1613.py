# Generated by Django 2.0.3 on 2018-06-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='adhaar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='alt_contact',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='blood_group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
    ]

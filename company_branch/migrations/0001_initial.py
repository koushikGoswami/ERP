# Generated by Django 2.0.3 on 2018-05-07 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0006_auto_20180507_1824'),
        ('states', '0006_auto_20180507_1514'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_address', models.CharField(max_length=100)),
                ('branch_city', models.CharField(max_length=100)),
                ('branch_pincode', models.CharField(max_length=50)),
                ('branch_contact_no', models.BigIntegerField()),
                ('branch_email', models.EmailField(max_length=50)),
                ('branch_gstin', models.CharField(max_length=50)),
                ('branch_pan', models.CharField(max_length=50)),
                ('branch_cin', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='states.State')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 2.0.3 on 2018-05-15 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0003_auto_20180515_1409'),
        ('company', '0008_auto_20180514_1542'),
        ('purchase_requisition', '0004_auto_20180515_1113'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchaseorggroup', '0003_auto_20180509_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_no', models.CharField(max_length=255)),
                ('quotation_date', models.DateTimeField(auto_now_add=True)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('grand_total_words', models.CharField(max_length=255)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_finalised', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('pur_grp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchaseorggroup.PurchaseGroup')),
                ('pur_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchaseorggroup.PurchaseOrg')),
                ('requisition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase_requisition.Requisition')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.Vendor')),
                ('vendor_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.VendorAddress')),
            ],
        ),
    ]

# Generated by Django 2.0.3 on 2018-05-11 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchaseorggroup', '0003_auto_20180509_1712'),
        ('company_branch', '0005_auto_20180509_1743'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_fullname', models.CharField(max_length=100)),
                ('material_code', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('is_taxable', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material_Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_for', models.CharField(choices=[('1', 'Purchase'), ('2', 'Sales')], default='1', max_length=1)),
                ('igst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cgst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sgst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hsn', models.CharField(max_length=30)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_tax', to='material_master.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Material_UOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_for', models.CharField(choices=[('1', 'Purchase'), ('2', 'Sales')], default='1', max_length=1)),
                ('unit_per_uom', models.DecimalField(decimal_places=2, max_digits=10)),
                ('base_uom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='base_uom', to='company_branch.UOM')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_uom', to='material_master.Material')),
                ('unit_uom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unit_uom', to='company_branch.UOM')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialPurchaseGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_purchase_grp', to='material_master.Material')),
                ('pur_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchaseorggroup.PurchaseGroup')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialPurchaseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_purchase_org', to='material_master.Material')),
                ('pur_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchaseorggroup.PurchaseOrg')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='material_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='material_master.MaterialType'),
        ),
    ]
# Generated by Django 2.0.3 on 2018-05-16 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_invoice', '0002_purchaseinvoicedetail_purchaseinvoicemap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoicedetail',
            name='pur_invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur_invoice_detail', to='purchase_invoice.PurchaseInvoice'),
        ),
    ]
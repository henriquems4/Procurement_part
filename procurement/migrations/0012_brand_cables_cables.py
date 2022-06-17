# Generated by Django 4.0.4 on 2022-06-17 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0011_brand_acessories_alter_inverter_acessories_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand_cables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=150)),
                ('vendor_name', models.CharField(max_length=100)),
                ('vendor_contact', models.CharField(max_length=100)),
                ('vendor_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cables_id', models.CharField(default='06.CAB-01', max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=30)),
                ('payment_conditions', models.TextField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='marcas_cables', to='procurement.brand_cables')),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-14 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0007_alter_pv_modules_modules_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='inverters_brand',
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
            name='inverters_power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_id', models.CharField(max_length=50)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='inverters',
            old_name='inventory',
            new_name='price_CIF',
        ),
        migrations.RenameField(
            model_name='inverters',
            old_name='price',
            new_name='price_DDP',
        ),
        migrations.RemoveField(
            model_name='inverters',
            name='vendor',
        ),
        migrations.AddField(
            model_name='inverters',
            name='inverters_id',
            field=models.CharField(default='04.INV-01', max_length=50),
        ),
        migrations.AddField(
            model_name='inverters',
            name='payment_conditions',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inverters',
            name='price_EXW',
            field=models.FloatField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inverters',
            name='price_FOB',
            field=models.FloatField(default=3, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inverters',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inverters',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='marcas_modules', to='procurement.inverters_brand'),
        ),
        migrations.AlterField(
            model_name='inverters',
            name='power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='power_modules', to='procurement.inverters_power'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0003_pv_modules_power_pv_modules_modules_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pv_modules',
            old_name='inventory',
            new_name='price_CIF',
        ),
        migrations.RenameField(
            model_name='pv_modules',
            old_name='price',
            new_name='price_DPP',
        ),
        migrations.AddField(
            model_name='pv_modules',
            name='payment_conditions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pv_modules',
            name='price_EXW',
            field=models.FloatField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pv_modules',
            name='price_FOB',
            field=models.FloatField(default=12, max_length=30),
            preserve_default=False,
        ),
    ]

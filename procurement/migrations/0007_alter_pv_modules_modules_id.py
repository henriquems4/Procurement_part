# Generated by Django 4.0.4 on 2022-06-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0006_rename_price_dpp_pv_modules_price_ddp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pv_modules',
            name='modules_id',
            field=models.CharField(default='03.PVM-01', max_length=50),
        ),
    ]

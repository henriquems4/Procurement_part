# Generated by Django 4.0.5 on 2022-06-07 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ac_cable',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=30)),
                ('inventory', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='construction',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('payment_conditions', models.TextField()),
                ('price', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_construction', to='procurement.brand')),
            ],
        ),
        migrations.CreateModel(
            name='dc_cable',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=30)),
                ('inventory', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_dccable', to='procurement.brand')),
            ],
        ),
        migrations.CreateModel(
            name='inverter_acessories',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=30)),
                ('inventory', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_acessories', to='procurement.brand')),
            ],
        ),
        migrations.CreateModel(
            name='inverters',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('power', models.FloatField()),
                ('price', models.FloatField(max_length=30)),
                ('inventory', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_inverters', to='procurement.brand')),
            ],
        ),
        migrations.CreateModel(
            name='order_ac_cables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
                ('ac_cables_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_ac_cable', to='procurement.ac_cable')),
            ],
        ),
        migrations.CreateModel(
            name='order_construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
                ('construction_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_inverters', to='procurement.construction')),
            ],
        ),
        migrations.CreateModel(
            name='order_dc_cables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
                ('dc_cables_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_dc_cable', to='procurement.dc_cable')),
            ],
        ),
        migrations.CreateModel(
            name='order_inverter1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
                ('inverter_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_inverters', to='procurement.inverters')),
            ],
        ),
        migrations.CreateModel(
            name='order_inverter_acessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
                ('inverter_acessories_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_inverters_acessories', to='procurement.inverter_acessories')),
            ],
        ),
        migrations.CreateModel(
            name='order_others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='order_pv_modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='order_structures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='pv_module_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=150)),
                ('vendor_name', models.CharField(max_length=100)),
                ('vendor_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='structures',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=30)),
                ('type', models.CharField(choices=[('Roof In-plane', 'roof in-plane'), ('Roof Ballast', 'roof ballast'), ('Roof 15ºTilt', 'roof 15ºtilt'), ('Ground 30ºTilt', 'ground 30ºtilt'), ('Ground Ballast', 'ground ballast'), ('Tracker', 'tracker')], max_length=50)),
                ('inventory', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_structures', to='procurement.brand')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_structures', to='procurement.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='pv_modules',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('power_range', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=30)),
                ('inventory', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='marcas_modules', to='procurement.pv_module_brand')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('total_power_ac', models.FloatField(max_length=50)),
                ('total_peak_power', models.FloatField(max_length=50)),
                ('location', models.CharField(max_length=75)),
                ('tilt', models.CharField(blank=True, max_length=75)),
                ('available_area', models.FloatField(max_length=30)),
                ('usable_area', models.FloatField(max_length=30)),
                ('order_ac_cables', models.ManyToManyField(blank=True, to='procurement.order_ac_cables')),
                ('order_construction', models.ManyToManyField(blank=True, to='procurement.order_construction')),
                ('order_dc_cables', models.ManyToManyField(blank=True, to='procurement.order_dc_cables')),
                ('order_inverter', models.ManyToManyField(blank=True, to='procurement.order_inverter1')),
                ('order_inverter_acessories', models.ManyToManyField(blank=True, to='procurement.order_inverter_acessories')),
                ('order_others', models.ManyToManyField(blank=True, to='procurement.order_others')),
                ('order_pv_modules', models.ManyToManyField(blank=True, to='procurement.order_pv_modules')),
                ('order_structures', models.ManyToManyField(blank=True, to='procurement.order_structures')),
            ],
        ),
        migrations.CreateModel(
            name='others',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('type', models.TextField()),
                ('price', models.FloatField(max_length=30)),
                ('inventory', models.FloatField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_other', to='procurement.brand')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_others', to='procurement.vendor')),
            ],
        ),
        migrations.AddField(
            model_name='order_structures',
            name='structures_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_structures', to='procurement.structures'),
        ),
        migrations.AddField(
            model_name='order_pv_modules',
            name='pv_modules_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_pv_modules', to='procurement.pv_modules'),
        ),
        migrations.AddField(
            model_name='order_others',
            name='others_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_of_others', to='procurement.others'),
        ),
        migrations.AddField(
            model_name='inverters',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_inverters', to='procurement.vendor'),
        ),
        migrations.AddField(
            model_name='inverter_acessories',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_acessories', to='procurement.vendor'),
        ),
        migrations.AddField(
            model_name='dc_cable',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_dccable', to='procurement.vendor'),
        ),
        migrations.AddField(
            model_name='construction',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_construction', to='procurement.vendor'),
        ),
        migrations.AddField(
            model_name='ac_cable',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marcas_accable', to='procurement.brand'),
        ),
        migrations.AddField(
            model_name='ac_cable',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores_accable', to='procurement.vendor'),
        ),
    ]

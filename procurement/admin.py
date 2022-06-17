from django.contrib import admin
from .models import vendor,brand,inverters,pv_modules,construction,structures,inverter_acessories,project,order_inverter1,order_structures,order_construction,order_others,order_pv_modules,order_inverter_acessories,\
    order_ac_cables,order_dc_cables,pv_module_brand,pv_modules_power,inverters_brand,inverters_power,inv_acessorie_type,brand_acessories,cables,cable_information,brand_cables,type_cable

@admin.register(brand)
class invertersadmin(admin.ModelAdmin):
    pass


@admin.register(inverters)
class invertersadmin(admin.ModelAdmin):
    pass

@admin.register(inverters_brand)
class inverter_brandadmin(admin.ModelAdmin):
    pass

@admin.register(inverters_power)
class inverter_poweradmin(admin.ModelAdmin):
    pass


@admin.register(pv_module_brand)
class pv_modules_brandadmin(admin.ModelAdmin):
    pass

@admin.register(pv_modules_power)
class pv_modules_power_brandadmin(admin.ModelAdmin):
    pass


@admin.register(pv_modules)
class invertersadmin(admin.ModelAdmin):
    pass

@admin.register(inv_acessorie_type)
class inv_acessories_type(admin.ModelAdmin):
    pass

@admin.register(brand_acessories)
class inv_acessories_brand(admin.ModelAdmin):
    pass

@admin.register(inverter_acessories)
class inv_acessories(admin.ModelAdmin):
    pass

@admin.register(cables)
class cables(admin.ModelAdmin):
    pass

@admin.register(cable_information)
class cable_information(admin.ModelAdmin):
    pass

@admin.register(type_cable)
class cable_type(admin.ModelAdmin):
    pass

@admin.register(brand_cables)
class cable_brand(admin.ModelAdmin):
    pass





@admin.register(vendor)
class invertersadmin(admin.ModelAdmin):
    pass



@admin.register(construction)
class constructuresadmin(admin.ModelAdmin):
    pass
# Register your models here.


@admin.register(order_inverter1)
class order_invertersadmin(admin.ModelAdmin):
    pass

@admin.register(order_others)
class order_othersadmin(admin.ModelAdmin):
    pass

@admin.register(order_pv_modules)
class order_pv_modulesadmin(admin.ModelAdmin):
    pass

@admin.register(order_inverter_acessories)
class order_inverter_acessoriesadmin(admin.ModelAdmin):
    pass

@admin.register(order_construction)
class order_constructionadmin(admin.ModelAdmin):
    pass

@admin.register(order_structures)
class order_structuresadmin(admin.ModelAdmin):
    pass

@admin.register(order_dc_cables)
class order_dc_cablesadmin(admin.ModelAdmin):
    pass

@admin.register(order_ac_cables)
class order_ac_cablesadmin(admin.ModelAdmin):
    pass

@admin.register(project)
class projectadmin(admin.ModelAdmin):
    pass

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



"""*****Total Brands*****"""
class brand(models.Model):
    brand_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    def __str__(self):
        return self.name


"""*****PV Modules Part******"""

#Brands specific for PV Modules
class pv_module_brand(models.Model):
    brand_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#Foreign key for the PV modules power
class pv_modules_power(models.Model):
    power_id = models.CharField(max_length=50)
    power = models.IntegerField()
    def __str__(self):
        return str(self.power)

#Pv Modules model
class pv_modules(models.Model):
    modules_id = models.CharField(max_length=50,default='03.PVM-01')
    brand = models.ForeignKey(pv_module_brand, on_delete=models.SET_NULL, related_name='marcas_modules',blank=True,null=True)
    product_name = models.CharField(max_length=50)
    power_range = models.ForeignKey(pv_modules_power,on_delete=models.SET_NULL, related_name='power_modules',blank=True,null=True)
    price_EXW = models.FloatField(max_length=30)
    price_CIF = models.FloatField(max_length=30)
    price_DDP = models.FloatField(max_length=30)
    price_FOB = models.FloatField(max_length=30)
    payment_conditions = models.TextField()
    def __str__(self):
        return self.modules_id

"""*****Inverters Part******"""

#Brands specific for Inverters
class inverters_brand(models.Model):
    brand_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    def __str__(self):
        return self.name


#Foreign key for the Inverters power
class inverters_power(models.Model):
    power_id = models.CharField(max_length=50)
    power = models.IntegerField()
    def __str__(self):
        return str(self.power)

#Inverters model
class inverters(models.Model):
    inverters_id = models.CharField(max_length=50,default='04.INV-01')
    brand = models.ForeignKey(inverters_brand, on_delete=models.SET_NULL, related_name='marcas_modules',blank=True,null=True)
    product_name = models.CharField(max_length=50)
    power = models.ForeignKey(inverters_power,on_delete=models.SET_NULL, related_name='power_modules',blank=True,null=True)
    price_EXW = models.FloatField(max_length=30)
    price_CIF = models.FloatField(max_length=30)
    price_DDP = models.FloatField(max_length=30)
    price_FOB = models.FloatField(max_length=30)
    payment_conditions = models.TextField()
    def __str__(self):
        return self.inverters_id

"""*****Inverter Acessories Part*****"""

class brand_acessories(models.Model):
    brand_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class inv_acessorie_type(models.Model):
    type_id = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    def __str__(self):
        return str(self.type)

class inverter_acessories(models.Model):
    acessorie_id = models.CharField(max_length=50, default='05.ACC-01')
    brand = models.ForeignKey(brand_acessories,on_delete=models.SET_NULL,blank=True,null=True, related_name='marcas_acessories')
    product_name = models.CharField(max_length=50)
    type = models.ForeignKey(inv_acessorie_type,on_delete=models.SET_NULL,blank=True,null=True, related_name='marcas_acessories')
    price = models.FloatField(max_length=30)
    payment_conditions = models.TextField()
    def __str__(self):
        return self.product_name

"""*****Cables Part*****"""

class brand_cables(models.Model):
    brand_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class type_cable(models.Model):
    type_id = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type

class cable_information(models.Model):
    information_id = models.CharField(max_length=20)
    information = models.CharField(max_length=80)
    type_cable = models.ForeignKey(type_cable,on_delete=models.SET_NULL,blank=True,null=True,related_name='tipo_cabo')

class cables(models.Model):
    cables_id = models.CharField(max_length=50, default='06.CAB-01')
    type = models.ForeignKey(type_cable,on_delete=models.SET_NULL,blank=True,null=True, related_name='tipo_cables')
    information = models.ForeignKey(cable_information, on_delete=models.SET_NULL, blank=True, null=True, related_name='information_cables')
    brand = models.ForeignKey(brand_cables,on_delete=models.SET_NULL,blank=True,null=True, related_name='marcas_cables')
    product_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    payment_conditions = models.TextField()
    def __str__(self):
        return self.product_name

"""***** Structures *****"""
class type_structure(models.Model):
    type_id = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type

class subtype_structure(models.Model):
    subtype_id = models.CharField(max_length=20)
    subtype = models.CharField(max_length=80)
    type_structure = models.ForeignKey(type_structure,on_delete=models.SET_NULL,blank=True,null=True,related_name='tipo_estrutura')

    def __str__(self):
        return self.subtype

class brand_structures(models.Model):
    brand_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class structures(models.Model):
    structures_id = models.CharField(max_length=50, default='07.STR-01')
    type = models.ForeignKey(type_structure, on_delete=models.SET_NULL, blank=True, null=True, related_name='type_estrutura')
    subtype = models.ForeignKey(subtype_structure, on_delete=models.SET_NULL, blank=True, null=True, related_name='subtype_estrutura')
    brand = models.ForeignKey(brand_structures,on_delete=models.SET_NULL,blank=True,null=True, related_name='marcas_estrutura')
    product_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    payment_conditions = models.TextField()
    def __str__(self):
        return self.product_name


"""******************************"""

class vendor(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


"""class inverters(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, related_name='marcas_inverters')
    product_name = models.CharField(max_length=50)
    power = models.FloatField()
    vendor = models.ForeignKey(vendor,on_delete=models.CASCADE, related_name='vendedores_inverters')
    price = models.FloatField(max_length=30)
    inventory = models.FloatField(max_length=30)"""



class construction(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, related_name='marcas_construction')
    product_name = models.CharField(max_length=50)
    payment_conditions = models.TextField()
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE, related_name='vendedores_construction')
    price = models.FloatField(max_length=30)
    def __str__(self):
        return self.product_name




class ac_cable(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, related_name='marcas_accable')
    product_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE, related_name='vendedores_accable')
    price = models.FloatField(max_length=30)
    inventory = models.FloatField(max_length=30)
    def __str__(self):
        return self.product_name

class dc_cable(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, related_name='marcas_dccable')
    product_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE, related_name='vendedores_dccable')
    price = models.FloatField(max_length=30)
    inventory = models.FloatField(max_length=30)
    def __str__(self):
        return self.product_name

class others(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, related_name='marcas_other')
    product_name = models.CharField(max_length=50)
    type = models.TextField()
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE, related_name='vendedores_others')
    price = models.FloatField(max_length=30)
    inventory = models.FloatField(max_length=30)
    def __str__(self):
        return self.product_name

class order_inverter1(models.Model):
    inverter_number=models.ForeignKey(inverters,on_delete=models.CASCADE,related_name='order_of_inverters')
    quantity=models.FloatField(max_length=30)

class order_construction(models.Model):
    construction_number=models.ForeignKey(construction,on_delete=models.CASCADE,related_name='order_of_inverters')
    quantity=models.FloatField(max_length=30)

class order_pv_modules(models.Model):
    pv_modules_number=models.ForeignKey(pv_modules,on_delete=models.CASCADE,related_name='order_of_pv_modules')
    quantity=models.FloatField(max_length=30)

class order_inverter_acessories (models.Model):
    inverter_acessories_number=models.ForeignKey(inverter_acessories,on_delete=models.CASCADE,related_name='order_of_inverters_acessories')
    quantity=models.FloatField(max_length=30)

class order_structures (models.Model):
    structures_number=models.ForeignKey(structures,on_delete=models.CASCADE,related_name='order_of_structures')
    quantity=models.FloatField(max_length=30)

class order_dc_cables (models.Model):
    dc_cables_number=models.ForeignKey(dc_cable,on_delete=models.CASCADE,related_name='order_of_dc_cable')
    quantity=models.FloatField(max_length=30)

class order_ac_cables (models.Model):
    ac_cables_number=models.ForeignKey(ac_cable,on_delete=models.CASCADE,related_name='order_of_ac_cable')
    quantity=models.FloatField(max_length=30)

class order_others (models.Model):
    others_number=models.ForeignKey(others,on_delete=models.CASCADE,related_name='order_of_others')
    quantity=models.FloatField(max_length=30)

class project(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    total_power_ac = models.FloatField(max_length=50)
    total_peak_power = models.FloatField(max_length=50)
    #delivery_time= models.DateField(blank=True)
    location=models.CharField(max_length=75)
    tilt=models.CharField(max_length=75,blank=True)
    available_area=models.FloatField(max_length=30)
    usable_area = models.FloatField(max_length=30)
    order_inverter = models.ManyToManyField(order_inverter1, blank=True)
    order_inverter_acessories = models.ManyToManyField(order_inverter_acessories, blank=True)
    order_others = models.ManyToManyField(order_others, blank=True)
    order_structures = models.ManyToManyField(order_structures, blank=True)
    order_construction = models.ManyToManyField(order_construction, blank=True)
    order_pv_modules = models.ManyToManyField(order_pv_modules, blank=True)
    order_dc_cables = models.ManyToManyField(order_dc_cables, blank=True)
    order_ac_cables = models.ManyToManyField(order_ac_cables, blank=True)

from .models import brand,vendor,brand_acessories,construction,pv_modules,ac_cable,dc_cable,brand_structures,inverter_acessories,others,project,order_inverter1,order_pv_modules,order_construction,order_inverter_acessories,order_structures,order_ac_cables,order_dc_cables,order_others,pv_module_brand,inverters_brand,brand_cables
from django import forms
from django import template

register = template.Library()

class brand_creation(forms.ModelForm):
    class Meta:
        model = brand
        fields = {'brand_id', 'name', 'link', 'vendor_name', 'vendor_contact', 'vendor_email'}
        labels = {
            'brand_id': 'Brand ID (xx):',
        }
    field_order = ['brand_id', 'name', 'link', 'vendor_name', 'vendor_contact', 'vendor_email']

class vendor_creation(forms.ModelForm):
    class Meta:
        model = vendor
        fields = {'name','contact','email'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input1'}),
            'contact': forms.TextInput(attrs={'class': 'input1'}),
            'email': forms.TextInput(attrs={'class': 'input1'}),
        }
    field_order = ['name','contact','email']

class brand_pv_modules_creation(forms.ModelForm):
    class Meta:
        model = pv_module_brand
        fields = {'brand_id','name','link','vendor_name','vendor_contact','vendor_email'}
        labels = {
            'brand_id': 'Brand ID (xx):',
        }
    field_order = ['brand_id','name','link','vendor_name','vendor_contact','vendor_email']


class brand_inverters_creation(forms.ModelForm):
    class Meta:
        model = inverters_brand
        fields = {'brand_id','name','link','vendor_name','vendor_contact','vendor_email'}
        labels = {
            'brand_id': 'Brand ID (xx):',
        }
    field_order = ['brand_id','name','link','vendor_name','vendor_contact','vendor_email']

class brand_inverters_acessories_creation(forms.ModelForm):
    class Meta:
        model = brand_acessories
        fields = {'brand_id','name','link','vendor_name','vendor_contact','vendor_email'}
        labels = {
            'brand_id': 'Brand ID (xx):',
        }
    field_order = ['brand_id','name','link','vendor_name','vendor_contact','vendor_email']

class brand_cables_creation(forms.ModelForm):
    class Meta:
        model = brand_cables
        fields = {'brand_id','name','link','vendor_name','vendor_contact','vendor_email'}
        labels = {
            'brand_id': 'Brand ID (xx):',
        }
    field_order = ['brand_id','name','link','vendor_name','vendor_contact','vendor_email']



class brand_structures_creation(forms.ModelForm):
    class Meta:
        model = brand_structures
        fields = {'brand_id','name','link','vendor_name','vendor_contact','vendor_email'}
        labels = {
            'brand_id': 'Brand ID (xx):',
        }
    field_order = ['brand_id','name','link','vendor_name','vendor_contact','vendor_email']


class construction_creation(forms.ModelForm):
    class Meta:
        model = construction
        fields = {'id', 'brand', 'product_name', 'payment_conditions', 'vendor', 'price'}
        widgets = {
            'id': forms.TextInput(attrs={'class': 'input1'}),
            'product_name': forms.TextInput(attrs={'class': 'input1'}),
            'payment_conditions': forms.TextInput(attrs={'class': 'input1'}),
            'vendor': forms.Select(attrs={'class': 'bootstrap-select'}),
            'brand': forms.Select(attrs={'class': 'bootstrap-select'}),
            'price': forms.TextInput(attrs={'class': 'input1'}),
        }
        labels = {
            'product_name': 'Service Designation',
            'price': 'Price (€)',
        }
    field_order = ['id', 'product_name', 'payment_conditions', 'vendor', 'brand', 'price']





class ac_cable_creation(forms.ModelForm):
    class Meta:
        model = ac_cable
        fields = {'id', 'brand', 'product_name', 'type', 'vendor', 'price', 'inventory'}
        widgets = {
            'id': forms.TextInput(attrs={'class': 'input1'}),
            'product_name': forms.TextInput(attrs={'class': 'input1'}),
            'type': forms.TextInput(attrs={'class': 'input1'}),
            'vendor': forms.Select(attrs={'class': 'bootstrap-select'}),
            'brand': forms.Select(attrs={'class': 'bootstrap-select'}),
            'price': forms.TextInput(attrs={'class': 'input1'}),
            'inventory': forms.TextInput(attrs={'class': 'input1'}),
        }
        labels = {
            'price': 'Price (€/m)',
            'inventory': 'Stock',
        }
    field_order = ['id', 'product_name', 'type', 'vendor', 'brand', 'price', 'inventory']

class dc_cable_creation(forms.ModelForm):
    class Meta:
        model = dc_cable
        fields = {'id', 'brand', 'product_name', 'type', 'vendor', 'price', 'inventory'}
        widgets = {
            'id': forms.TextInput(attrs={'class': 'input1'}),
            'product_name': forms.TextInput(attrs={'class': 'input1'}),
            'type': forms.TextInput(attrs={'class': 'input1'}),
            'vendor': forms.Select(attrs={'class': 'bootstrap-select'}),
            'brand': forms.Select(attrs={'class': 'bootstrap-select'}),
            'price': forms.TextInput(attrs={'class': 'input1'}),
            'inventory': forms.TextInput(attrs={'class': 'input1'}),
        }
        labels = {
            'price': 'Price (€/m)',
            'inventory': 'Stock',
        }
    field_order = ['id', 'product_name', 'type', 'vendor', 'brand', 'price', 'inventory']

class others_creation(forms.ModelForm):
    class Meta:
        model = others
        fields = {'id', 'brand', 'product_name', 'type', 'vendor', 'price', 'inventory'}
        widgets = {
            'id': forms.TextInput(attrs={'class': 'input1'}),
            'product_name': forms.TextInput(attrs={'class': 'input1'}),
            'vendor': forms.Select(attrs={'class': 'bootstrap-select'}),
            'brand': forms.Select(attrs={'class': 'bootstrap-select'}),
            'type': forms.TextInput(attrs={'class': 'input1'}),
            'price': forms.TextInput(attrs={'class': 'input1'}),
            'inventory': forms.TextInput(attrs={'class': 'input1'}),
        }
        labels = {
            'price': 'Price (€)',
            'inventory': 'Stock',
        }
    field_order = ['id', 'product_name', 'type', 'vendor', 'brand', 'price', 'inventory']



class project_creation(forms.ModelForm):
    """delivery_time = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class':'input1'
            }),
        input_formats=('%Y-%m-%d',),
    )"""

    class Meta:
        model = project
        fields = {'id', 'name','total_power_ac','total_peak_power','location','tilt','available_area','usable_area'}
        widgets = {
            'id': forms.TextInput(attrs={'class': 'input1'}),
            'name': forms.TextInput(attrs={'class': 'input1'}),
            'total_power_ac': forms.TextInput(attrs={'class': 'input1'}),
            'total_peak_power': forms.TextInput(attrs={'class': 'input1'}),
            'tilt': forms.TextInput(attrs={'class': 'input1'}),
            'available_area': forms.TextInput(attrs={'class': 'input1'}),
            'usable_area': forms.TextInput(attrs={'class': 'input1'}),
            'location': forms.TextInput(attrs={'class': 'input1'}),
        }
        labels = {
            'id':'Project Number',
            'total_power_ac': 'Total Power AC (kWac)',
            'total_peak_power': 'Total Peak Power (kWp)',
            'available_area':'Available Area (m2)',
            'usable_area':'Usable Area (m2)',
        }


    field_order = ['id', 'name','total_power_ac','total_peak_power','location','tilt','available_area','usable_area']

#    def __init__(self, *args, **kwargs):
#        super(project_creation, self).__init__(*args, **kwargs)
#        for field_name, field in self.fields.items():
#            field.widget.attrs['class'] = 'input1'


class number_form_inverter(forms.ModelForm):
    class Meta:
        model = order_inverter1
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_pv_modules(forms.ModelForm):
    class Meta:
        model = order_pv_modules
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_construction(forms.ModelForm):
    class Meta:
        model = order_construction
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }


class number_form_inverter_acessories(forms.ModelForm):
    class Meta:
        model = order_inverter_acessories
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_structures(forms.ModelForm):
    class Meta:
        model = order_structures
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_ac_cables(forms.ModelForm):
    class Meta:
        model = order_ac_cables
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_dc_cables(forms.ModelForm):
    class Meta:
        model = order_dc_cables
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_others(forms.ModelForm):
    class Meta:
        model = order_others
        fields = {'quantity'}
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

"""class number_form_inverter1(forms.ModelForm):
    class Meta:
        model = order_inverter1
        fields = {'inverter_number','quantity'}
        widgets = {
            'inverter_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_pv_modules1(forms.ModelForm):
    class Meta:
        model = order_pv_modules
        fields = {'pv_modules_number','quantity'}
        widgets = {
            'pv_modules_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_construction1(forms.ModelForm):
    class Meta:
        model = order_construction
        fields = {'construction_number','quantity'}
        widgets = {
            'construction_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }


class number_form_inverter_acessories1(forms.ModelForm):
    class Meta:
        model = order_inverter_acessories
        fields = {'inverter_acessories_number','quantity'}
        widgets = {
            'inverter_acessories_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_structures1(forms.ModelForm):
    class Meta:
        model = order_structures
        fields = {'structures_number','quantity'}
        widgets = {
            'structures_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_ac_cables1(forms.ModelForm):
    class Meta:
        model = order_ac_cables
        fields = {'ac_cables_number','quantity'}
        widgets = {
            'ac_cables_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_dc_cables1(forms.ModelForm):
    class Meta:
        model = order_dc_cables
        fields = {'dc_cables_number','quantity'}
        widgets = {
            'dc_cables_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }

class number_form_others1(forms.ModelForm):
    class Meta:
        model = order_others
        fields = {'others_number','quantity'}
        widgets = {
            'others_number': forms.TextInput(attrs={'class': 'input2'}),
            'quantity': forms.TextInput(attrs={'class': 'input2'}),
        }
"""

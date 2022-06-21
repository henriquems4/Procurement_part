from django.shortcuts import render,get_object_or_404,redirect
from .models import vendor,inverters,construction,pv_modules,ac_cable,dc_cable,cables,cable_information,type_cable,brand_cables,structures,inverter_acessories,others,order_inverter1,project,order_pv_modules,order_construction,order_inverter_acessories,order_structures,order_ac_cables,order_dc_cables,order_others,pv_modules_power,pv_module_brand,inverters_brand,inverters_power,inv_acessorie_type,brand,brand_acessories,brand_structures,subtype_structure,type_structure
from django.http import HttpResponseRedirect,HttpResponse
from .forms import brand_creation,vendor_creation,construction_creation,brand_inverters_acessories_creation,ac_cable_creation,dc_cable_creation,others_creation,project_creation,number_form_inverter,number_form_pv_modules,number_form_construction,number_form_inverter_acessories,number_form_structures,number_form_ac_cables,number_form_dc_cables,number_form_others,brand_pv_modules_creation,brand_inverters_creation,brand_cables_creation,brand_structures_creation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import datetime


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Username or Password is incorrect')

    context =  {}
    return render(request, 'procurement/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/login')


"""*****PV Modules Creation*****"""

@login_required(login_url='/login')
def brand_module_(request):
    form = brand_pv_modules_creation()
    if request.method == 'POST':
        modules_form=brand_pv_modules_creation(data=request.POST)
        if modules_form.is_valid():
            new_module=modules_form.save(commit=False)
            new_module.save()
            return HttpResponseRedirect ('/pv_modules/',{'message':'Module Saved'})
    guardar='Save Module Brand'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/pv_module_update.html',context)


#Creation of the PV Modules
"""needed:
1- Information that this part is already created
2- Error messages when something is going bad"""
@login_required(login_url='/login')
def pv_modules_(request):
    new_pv_module= None
    name_part = 'PV Module Creation'
    name_save = 'Save PV Module'
    brand_options=pv_module_brand.objects.all()
    power_options=pv_modules_power.objects.all()
    created = False
    done = ''
    if request.method == 'POST':
        try:
        #pv_module_form=pv_modules_creation(data=request.POST)
            modules_id = request.POST.get('pv_module_id')
            brand = request.POST.get('brand')
            power_range = request.POST.get('power')
            product_name = request.POST.get('product_name')
            price_EXW = request.POST.get('price_EXW')
            price_CIF = request.POST.get('price_CIF')
            price_DDP = request.POST.get('price_DDP')
            price_FOB = request.POST.get('price_FOB')
            payment_conditions = request.POST.get('payment_conditions')
            marca = pv_module_brand.objects.get(brand_id=brand)
            potencia = pv_modules_power.objects.get(power_id=power_range)
            pv_modules.objects.create(modules_id=modules_id,brand=marca,product_name=product_name,power_range=potencia,price_EXW=float(price_EXW),price_CIF=float(price_CIF),price_DDP=float(price_DDP),price_FOB=float(price_FOB),payment_conditions=payment_conditions)
            created = True
            done = 'PV Module '+modules_id+' Saved with Sucess'
        except Exception as e:
            created = True
            done = 'Error: Values were wrong! Try Again!'
        #if pv_module_form.is_valid():
            #new_pv_module=pv_module_form.save(commit=False)
            #new_pv_module.save()
            #return HttpResponseRedirect ('/procurement/pv_modules/',{'message':'Inverter Saved'})
    #else:
        #pv_module_form=pv_modules_creation()
    return render(request, 'Procurement/procurement_part/pv_modules_form.html',{'name_save':name_save,'name_part':name_part,'brand_options':brand_options,'power_options':power_options,'created':created,'done':done})

"""*****Inverter Creation*****"""

@login_required(login_url='/login')
def brand_inverter_(request):
    form = brand_inverters_creation()
    if request.method == 'POST':
        inverters_form=brand_inverters_creation(data=request.POST)
        if inverters_form.is_valid():
            new_inverter=inverters_form.save(commit=False)
            new_inverter.save()
            return HttpResponseRedirect ('/inverters/',{'message':'Inverter Saved'})
    guardar='Save Inverter Brand'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/pv_module_update.html',context)




@login_required(login_url='/login')
def inverter_(request):
    new_inverter=None
    name_part = 'Inverter Creation'
    name_save = 'Save Inverter'
    brand_options = inverters_brand.objects.all()
    power_options = inverters_power.objects.all()
    created = False
    done = ''
    if request.method=='POST':
        try:
            inverters_id = request.POST.get('inverter_id')
            brand = request.POST.get('brand')
            power_range = request.POST.get('power')
            product_name = request.POST.get('product_name')
            price_EXW = request.POST.get('price_EXW')
            price_CIF = request.POST.get('price_CIF')
            price_DDP = request.POST.get('price_DDP')
            price_FOB = request.POST.get('price_FOB')
            payment_conditions = request.POST.get('payment_conditions')
            marca = inverters_brand.objects.get(brand_id=brand)
            potencia = inverters_power.objects.get(power_id=power_range)
            inverters.objects.create(inverters_id=inverters_id, brand=marca, product_name=product_name,
                                      power=potencia, price_EXW=float(price_EXW), price_CIF=float(price_CIF),
                                      price_DDP=float(price_DDP), price_FOB=float(price_FOB),
                                      payment_conditions=payment_conditions)
            created = True
            done = 'Inverter ' + inverters_id + ' Saved with Sucess'
        except:
            created = True
            done = 'Error: Values were wrong! Try Again!'
    return render(request, 'Procurement/procurement_part/inverters_form.html',
                  {'name_save': name_save, 'name_part': name_part, 'brand_options': brand_options,
                   'power_options': power_options, 'created': created, 'done': done})

"""*****Inverter Acessories Creation*****"""

@login_required(login_url='/login')
def brand_inverter_acessories_(request):
    form = brand_inverters_acessories_creation()
    if request.method == 'POST':
        inverters_acessories_form=brand_inverters_acessories_creation(data=request.POST)
        if inverters_acessories_form.is_valid():
            new_inverter_acessorie=inverters_acessories_form.save(commit=False)
            new_inverter_acessorie.save()
            return HttpResponseRedirect ('/inverter_acessories/',{'message':'Inverter acessorie Saved'})
    guardar='Save Inverter acessorie Brand'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/pv_module_update.html',context)



@login_required(login_url='/login')
def inverter_acessories_(request):
    new_inverter_acessorie= None
    name_part = 'Inverter Acessorie Creation'
    name_save = 'Save Inverter Acessorie'
    type_options = inv_acessorie_type.objects.all()
    brand_options=brand_acessories.objects.all()
    created = False
    done = ''
    if request.method == 'POST':
        try:
            inv_acessories_id = request.POST.get('inv_acessories_id')
            brand = request.POST.get('brand')
            type = request.POST.get('type')
            product_name = request.POST.get('product_name')
            price = request.POST.get('price')
            payment_conditions = request.POST.get('payment_conditions')
            marca = brand_acessories.objects.get(brand_id=brand)
            potencia = inv_acessorie_type.objects.get(type_id=type)
            inverter_acessories.objects.create(acessorie_id=inv_acessories_id, brand=marca, product_name=product_name,
                                     type=potencia, price=float(price),
                                     payment_conditions=payment_conditions)
            created = True
            done = 'Inverter Acessorie ' + inv_acessories_id + ' Saved with Sucess'
        except:
            created = True
            done = 'Error: Values were wrong! Try Again!'
    return render(request, 'Procurement/procurement_part/inverter_acessories_form.html',{'name_save':name_save,'name_part':name_part,'brand_options': brand_options,
                   'type_options': type_options, 'created': created, 'done': done})

"""*****Cables Creation*****"""
@login_required(login_url='/login')
def brand_cables_(request):
    form = brand_cables_creation()
    if request.method == 'POST':
        cables_form=brand_cables_creation(data=request.POST)
        if cables_form.is_valid():
            new_cable=cables_form.save(commit=False)
            new_cable.save()
            return HttpResponseRedirect ('/cables/',{'message':'Cable brand Saved'})
    guardar='Save cable Brand'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/pv_module_update.html',context)


@login_required(login_url='/login')
def cable(request):
    parts = cables.objects.all()
    return render(request,'Procurement/procurement_part/cables.html',{'cables':parts})

@login_required(login_url='/login')
def cables_(request):
    new_cable= None
    name_part = 'Cable Creation'
    name_save = 'Save Cable'
    type_options = type_cable.objects.all()
    brand_options = brand_cables.objects.all()
    information_option = cable_information.objects.all()
    created = False
    done = ''
    if request.method == 'POST':
        try:
            cables_id = request.POST.get('cable_id')
            brand = request.POST.get('brand')
            type = request.POST.get('type')
            product_name = request.POST.get('product_name')
            price = request.POST.get('price')
            payment_conditions = request.POST.get('payment_conditions')
            information = request.POST.get('information')
            print(information)
            marca = brand_cables.objects.get(brand_id=brand)
            cable_type = type_cable.objects.get(type_id=type)
            information_cable = cable_information.objects.get(information_id=information,type_cable=cable_type.id)
            cables.objects.create(cables_id=cables_id, brand=marca, product_name=product_name,
                                     type=cable_type, price=float(price),
                                     payment_conditions=payment_conditions,information=information_cable)
            created = True
            done = 'Cable ' + cables_id + ' Saved with Success'
        except:
            created = True
            done = 'Error: Values were wrong! Try Again!'
    return render(request, 'Procurement/procurement_part/cables_form.html',{'name_save':name_save,'name_part':name_part,'brand_options': brand_options,
                   'type_options': type_options,'information':information_option,'created': created, 'done': done})




@login_required(login_url='/login')
def delete_cable (request,pk):
    cable = cables.objects.get(id=pk)
    next = '/cables/'
    if request.method=="POST":
        cable.delete()
        return redirect(next)
    context = {'item':cable,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

"""***** Structure Creation *****"""

def brand_structures_(request):
    form = brand_structures_creation()
    if request.method == 'POST':
        structures_form=brand_structures_creation(data=request.POST)
        if structures_form.is_valid():
            new_structure=structures_form.save(commit=False)
            new_structure.save()
            return HttpResponseRedirect ('/structures/',{'message':'Structure brand Saved'})
    guardar='Save structure Brand'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/pv_module_update.html',context)

@login_required(login_url='/login')
def structure_(request):
    new_cable= None
    name_part = 'Structure Creation'
    name_save = 'Save Structure'
    type_options = type_structure.objects.all()
    brand_options = brand_structures.objects.all()
    information_option = subtype_structure.objects.all()
    created = False
    done = ''
    if request.method == 'POST':
        try:
            cables_id = request.POST.get('structure_id')
            brand = request.POST.get('brand')
            type = request.POST.get('type')
            product_name = request.POST.get('product_name')
            price = request.POST.get('price')
            payment_conditions = request.POST.get('payment_conditions')
            information = request.POST.get('information')
            marca = brand_structures.objects.get(brand_id=brand)
            structure_type = type_structure.objects.get(type_id=type)
            information_structure = subtype_structure.objects.get(subtype_id=information,type_structure=structure_type.id)
            structures.objects.create(structures_id=cables_id, brand=marca, product_name=product_name,
                                     type=structure_type, price=float(price),
                                     payment_conditions=payment_conditions,subtype=information_structure)
            created = True
            done = 'Structure ' + cables_id + ' Saved with Success'
        except Exception as e:
            print(e)
            #created = True
            #done = 'Error: Values were wrong! Try Again!'
    return render(request, 'Procurement/procurement_part/structures_form.html',{'name_save':name_save,'name_part':name_part,'brand_options': brand_options,
                   'type_options': type_options,'information':information_option,'created': created, 'done': done})

@login_required(login_url='/login')
def deletestructure(request,pk):
    structure = structures.objects.get(id=pk)
    next = '/structures/'
    if request.method=="POST":
        structure.delete()
        return redirect(next)
    context = {'item':structure,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)


"""*****Brand Creation*****"""

@login_required(login_url='/login')
def brand_(request):
    new_brand=None
    next=None
    if request.method == 'POST':
        brand_form=brand_creation(data=request.POST)
        if brand_form.is_valid():
            next2=request.POST.get('next')
            new_brand=brand_form.save(commit=False)
            new_brand.save()
            return HttpResponseRedirect(next2)
    else:
        brand_form=brand_creation()
        next = request.META.get('HTTP_REFERER')
    return render(request, 'Procurement/procurement_part/brands_creation.html', {'brand_form':brand_form, 'urlss':next})


@login_required(login_url='/login')
def brands(request):
    brands = brand.objects.all()
    return render(request,'Procurement/procurement_part/Brands.html',{'brands':brands})

@login_required(login_url='/login')
def updatebrand_(request ,pk):
    brands=brand.objects.get(id=pk)
    form = brand_creation(instance=brands)
    if request.method == 'POST':
        brands_form=brand_creation(data=request.POST,instance=brands)
        if brands_form.is_valid():
            new_brand=brands_form.save(commit=False)
            new_brand.save()
            return HttpResponseRedirect ('/brands/',{'message':'Brand Saved'})
    guardar='Update Brand'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def deletebrand(request,pk):
    brands = brand.objects.get(id=pk)
    next='/procurement/brands/'
    if request.method=="POST":
        brands.delete()
        return redirect(next)
    context = {'item':brands,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def vendor_(request):
    new_vendor=None
    next = None
    if request.method == 'POST':
        vendor_form=vendor_creation(data=request.POST)
        if vendor_form.is_valid():
            next2 = request.POST.get('next')
            new_vendor=vendor_form.save(commit=False)
            new_vendor.save()
            return HttpResponseRedirect(next2)
    else:
        vendor_form=vendor_creation()
        next = request.META.get('HTTP_REFERER')
    return render(request, 'Procurement/procurement_part/vendor_creation.html', {'vendor_form':vendor_form, 'urlss':next})

@login_required(login_url='/login')
def vendors(request):
    vendors = vendor.objects.all()
    return render(request,'Procurement/procurement_part/vendor.html',{'vendors':vendors})

@login_required(login_url='/login')
def updatevendor_(request ,pk):
    vendors=vendor.objects.get(id=pk)
    form = vendor_creation(instance=vendors)
    if request.method == 'POST':
        vendors_form=vendor_creation(data=request.POST,instance=vendors)
        if vendors_form.is_valid():
            new_vendor=vendors_form.save(commit=False)
            new_vendor.save()
            return HttpResponseRedirect ('/vendors/',{'message':'Vendor Saved'})
    guardar='Update Vendor'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def deletevendor(request,pk):
    vendors = vendor.objects.get(id=pk)
    next='/procurement/vendors/'
    if request.method=="POST":
        vendors.delete()
        return redirect(next)
    context = {'item':vendors,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)



@login_required(login_url='/login')
def ac_cables_(request):
    new_ac_cables= None
    name_part = 'Ac Cables Creation'
    name_save = 'Save Ac Cable'
    if request.method == 'POST':
        ac_cable_form=ac_cable_creation(data=request.POST)
        if ac_cable_form.is_valid():
            new_ac_cables=ac_cable_form.save(commit=False)
            new_ac_cables.save()
            return HttpResponseRedirect ('/ac_cables/',{'message':'Ac Cable Saved'})
    else:
        ac_cable_form=ac_cable_creation()
    return render(request, 'Procurement/procurement_part/creation.html',{'form':ac_cable_form,'name_save':name_save,'name_part':name_part})


@login_required(login_url='/login')
def dc_cables_(request):
    new_dc_cables= None
    name_part = 'Dc Cables Creation'
    name_save = 'Save Dc Cable'
    if request.method == 'POST':
        dc_cable_form=dc_cable_creation(data=request.POST)
        if dc_cable_form.is_valid():
            new_dc_cables=dc_cable_form.save(commit=False)
            new_dc_cables.save()
            return HttpResponseRedirect ('/dc_cables/',{'message':'Dc Cable Saved'})
    else:
        dc_cable_form=dc_cable_creation()
    return render(request, 'Procurement/procurement_part/creation.html',{'form':dc_cable_form,'name_save':name_save,'name_part':name_part})


@login_required(login_url='/login')
def others_(request):
    new_others= None
    name_part = 'Others Creation'
    name_save = 'Save Other'
    if request.method == 'POST':
        other_form=others_creation(data=request.POST)
        if other_form.is_valid():
            new_others=other_form.save(commit=False)
            new_others.save()
            return HttpResponseRedirect ('/others/',{'message':'Other Saved'})
    else:
        other_form=others_creation()
    return render(request, 'Procurement/procurement_part/creation.html',{'form':other_form,'name_save':name_save,'name_part':name_part})



"""@login_required(login_url='/login')
def updateinverter_(request ,pk):
    inverter=inverters.objects.get(id=pk)
    form = inverter_creation(instance=inverter)
    if request.method == 'POST':
        inverter_form=inverter_creation(data=request.POST,instance=inverter)
        if inverter_form.is_valid():
            new_inverter=inverter_form.save(commit=False)
            new_inverter.save()
            return HttpResponseRedirect ('/inverters/',{'message':'Inverter Saved'})
    guardar='Update Inverter'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)"""


@login_required(login_url='/login')
def updateother_(request ,pk):
    other=others.objects.get(id=pk)
    form = others_creation(instance=other)
    if request.method == 'POST':
        other_form=others_creation(data=request.POST,instance=other)
        if other_form.is_valid():
            new_other=other_form.save(commit=False)
            new_other.save()
            return HttpResponseRedirect ('/others/',{'message':'Other Saved'})
    guardar='Update Other'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)



@login_required(login_url='/login')
def deleteinverteracessorie(request,pk):
    inverter_acessorie = inverter_acessories.objects.get(id=pk)
    next='/inverter_acessories/'
    if request.method=="POST":
        inverter_acessorie.delete()
        return redirect(next)
    context = {'item':inverter_acessorie,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)


@login_required(login_url='/login')
def deleteinverter(request,pk):
    inverter = inverters.objects.get(id=pk)
    next = '/inverters/'
    if request.method=="POST":
        inverter.delete()
        return redirect(next)
    context = {'item':inverter,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)


@login_required(login_url='/login')
def deleteother (request,pk):
    other = others.objects.get(id=pk)
    next = '/others/'
    if request.method=="POST":
        other.delete()
        return redirect(next)
    context = {'item':other,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)




@login_required(login_url='/login')
def deletemodule (request,pk):
    modules = pv_modules.objects.get(id=pk)
    next='/pv_modules/'
    if request.method=="POST":
        modules.delete()
        return redirect(next)
    context = {'item':modules,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)


@login_required(login_url='/login')
def deleteconstruction (request,pk):
    constructions = construction.objects.get(id=pk)
    next = '/construction/'
    if request.method=="POST":
        constructions.delete()
        return redirect(next)
    context = {'item':constructions,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)


@login_required(login_url='/login')
def deleteac_cable (request,pk):
    ac_cables = ac_cable.objects.get(id=pk)
    next = '/ac_cables/'
    if request.method=="POST":
        ac_cables.delete()
        return redirect(next)
    context = {'item':ac_cables,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)


@login_required(login_url='/login')
def deletedc_cable (request,pk):
    dc_cables = dc_cable.objects.get(id=pk)
    next = '/dc_cables/'
    if request.method=="POST":
        dc_cables.delete()
        return redirect(next)
    context = {'item':dc_cables,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def updateconstruction_(request ,pk):
    constructions=construction.objects.get(id=pk)
    form = construction_creation(instance=constructions)
    if request.method == 'POST':
        construction_form=construction_creation(data=request.POST,instance=constructions)
        if construction_form.is_valid():
            new_construction=construction_form.save(commit=False)
            new_construction.save()
            return HttpResponseRedirect ('/construction/',{'message':'Construction Saved'})
    guardar='Update Construction'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)


"""@login_required(login_url='/login')
def updatestructure_(request ,pk):
    structure=structures.objects.get(id=pk)
    form = structures_creation(instance=structure)
    if request.method == 'POST':
        structure_form=structures_creation(data=request.POST,instance=structure)
        if structure_form.is_valid():
            new_structure=structure_form.save(commit=False)
            new_structure.save()
            return HttpResponseRedirect ('/structures/',{'message':'Structure Saved'})
    guardar='Update Structure'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)
"""


@login_required(login_url='/login')
def update_ac_cable_(request ,pk):
    ac_cables=ac_cable.objects.get(id=pk)
    form = ac_cable_creation(instance=ac_cables)
    if request.method == 'POST':
        ac_cable_form=ac_cable_creation(data=request.POST,instance=ac_cables)
        if ac_cable_form.is_valid():
            new_ac_cable=ac_cable_form.save(commit=False)
            new_ac_cable.save()
            return HttpResponseRedirect ('//ac_cables/',{'message':'Ac Cable Saved'})
    guardar='Update Ac Cable'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)


@login_required(login_url='/login')
def update_dc_cable_(request ,pk):
    dc_cables=dc_cable.objects.get(id=pk)
    form = dc_cable_creation(instance=dc_cables)
    if request.method == 'POST':
        dc_cable_form=dc_cable_creation(data=request.POST,instance=dc_cables)
        if dc_cable_form.is_valid():
            new_dc_cable=dc_cable_form.save(commit=False)
            new_dc_cable.save()
            return HttpResponseRedirect ('/dc_cables/',{'message':'Dc Cable Saved'})
    guardar='Update Dc Cable'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)





@login_required(login_url='/login')
def inventory_list(request):
    return render(request, 'Procurement/procurement_part/inventory_procurement.html')


@login_required(login_url='/login')
def success(request):
    return render(request,'Procurement/procurement_part/success.html')


@login_required(login_url='/login')
def inverter(request):
    inversores = inverters.objects.all()
    return render(request,'Procurement/procurement_part/inverters.html',{'inversores':inversores})


@login_required(login_url='/login')
def pv_module(request):
    parts = pv_modules.objects.all()
    return render(request,'Procurement/procurement_part/pv_modules.html',{'pv_module':parts})


@login_required(login_url='/login')
def constructions(request):
    parts = construction.objects.all()
    return render(request,'Procurement/procurement_part/construction.html',{'construction':parts})


@login_required(login_url='/login')
def ac_cables(request):
    parts = ac_cable.objects.all()
    return render(request, 'Procurement/procurement_part/cables.html', {'ac_cables':parts})


@login_required(login_url='/login')
def dc_cables(request):
    parts = dc_cable.objects.all()
    return render(request,'Procurement/procurement_part/dc_cables.html',{'dc_cables':parts})


@login_required(login_url='/login')
def structure(request):
    parts = structures.objects.all()
    return render(request,'Procurement/procurement_part/structures.html',{'structures':parts})


@login_required(login_url='/login')
def inverter_acessorie(request):
    parts = inverter_acessories.objects.all()
    return render(request,'Procurement/procurement_part/inverter_acessories.html',{'inverter_acessories':parts})


@login_required(login_url='/login')
def other(request):
    parts = others.objects.all()
    return render(request,'Procurement/procurement_part/others.html',{'others':parts})


@login_required(login_url='/login')
def constructions_(request):
    new_construction= None
    name_part = 'Construction Part Creation'
    name_save = 'Save Construction Part'
    if request.method == 'POST':
        construction_form=construction_creation(data=request.POST)
        if construction_form.is_valid():
            new_construction=construction_form.save(commit=False)
            new_construction.save()
            return HttpResponseRedirect ('/construction/',{'message':'Inverter Saved'})
    else:
        construction_form=construction_creation()
    return render(request, 'Procurement/procurement_part/creation.html',{'form':construction_form,'name_save':name_save,'name_part':name_part})


"""@login_required(login_url='/login')
def structures_(request):
    new_structure= None
    name_part = 'Structure Creation'
    name_save = 'Save Structure'
    if request.method == 'POST':
        structure_form=structures_creation(data=request.POST)
        if structure_form.is_valid():
            new_structure=structure_form.save(commit=False)
            new_structure.save()
            return HttpResponseRedirect ('/structures/',{'message':'Structure Saved'})
    else:
        structure_form=structures_creation()
    return render(request, 'Procurement/procurement_part/creation.html',{'form':structure_form,'name_save':name_save,'name_part':name_part})"""

@login_required(login_url='/login')
def projects(request):
    parts = project.objects.all()
    return render(request,'Procurement/procurement_part/projects.html',{'projects':parts})

@login_required(login_url='/login')
def project_(request):
    new_project= None
    name_part = 'Project Creation'
    name_save = 'Save Project'
    if request.method == 'POST':
        project_form=project_creation(data=request.POST)
        if project_form.is_valid():
            new_project=project_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/',{'message':'Project Saved'})
    else:
        project_form=project_creation()
    return render(request, 'Procurement/procurement_part/creation.html',{'form':project_form,'name_save':name_save,'name_part':name_part})

@login_required(login_url='/login')
def update_project(request ,pk):
    projects=project.objects.get(id=pk)
    form = project_creation(instance=projects)
    if request.method == 'POST':
        projects_form=project_creation(data=request.POST,instance=projects)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/',{'message':'Project Saved'})
    guardar='Update Project'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def deleteproject(request,pk):
    projects = project.objects.get(id=pk)
    next = '/projects/'
    if request.method=="POST":
        projects.delete()
        return redirect(next)
    context = {'item':projects,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

#Project details and orders

@login_required(login_url='/login')
def project_detail(request,pk):
    projects = project.objects.get(id=pk)
    inverter=projects.order_inverter.all()
    pv_modulos=projects.order_pv_modules.all()
    constructions=projects.order_construction.all()
    structure=projects.order_structures.all()
    inverter_acessorie=projects.order_inverter_acessories.all()
    ac_cables=projects.order_ac_cables.all()
    dc_cables=projects.order_dc_cables.all()
    other=projects.order_others.all()
    counter_inversores=0
    inverters_list_total = []
    for i in inverter:
        inverters_list = []
        counter_inversores += 1
        inverters_list.append(i.inverter_number_id)
        inversor=inverters.objects.get(id=i.inverter_number_id)
        inverters_list.append(inversor.product_name)
        inverters_list.append(inversor.power)
        inverters_list.append(i.quantity)
        inverters_list.append(i.id)
        inverters_list_total.append(inverters_list)
    counter_pv_modulos=0
    pv_modulos_list_total=[]
    for i in pv_modulos:
        pv_modulos_list = []
        counter_pv_modulos+=1
        pv_modulos_list.append(i.pv_modules_number_id)
        modulo=pv_modules.objects.get(id=i.pv_modules_number_id)
        pv_modulos_list.append(modulo.product_name)
        pv_modulos_list.append(modulo.power_range)
        pv_modulos_list.append(i.quantity)
        pv_modulos_list.append(i.id)
        pv_modulos_list_total.append(pv_modulos_list)
    counter_construction=0
    construction_list_total = []
    for i in constructions:
        construction_list = []
        counter_construction+=1
        construction_list.append(i.construction_number_id)
        constructions_data=construction.objects.get(id=i.construction_number_id)
        construction_list.append(constructions_data.product_name)
        construction_list.append(constructions_data.brand)
        construction_list.append(i.quantity)
        construction_list.append(i.id)
        construction_list_total.append(construction_list)
    counter_structures = 0
    structures_list_total = []
    for i in structure:
        counter_structures+=1
        structures_list = []
        structures_list.append(i.structures_number_id)
        structures_data=structures.objects.get(id=i.structures_number_id)
        structures_list.append(structures_data.product_name)
        structures_list.append(structures_data.type)
        structures_list.append(i.quantity)
        structures_list.append(i.id)
        structures_list_total.append(structures_list)
    counter_inv_acessories = 0
    inv_acessorie_list_total = []
    for i in inverter_acessorie:
        counter_inv_acessories += 1
        inv_acessorie_list = []
        inv_acessorie_list.append(i.inverter_acessories_number_id)
        inv_acessorie_data = inverter_acessories.objects.get(id=i.inverter_acessories_number_id)
        inv_acessorie_list.append(inv_acessorie_data.product_name)
        inv_acessorie_list.append(inv_acessorie_data.type)
        inv_acessorie_list.append(i.quantity)
        inv_acessorie_list.append(i.id)
        inv_acessorie_list_total.append(inv_acessorie_list)
    counter_ac_cable = 0
    ac_cable_list_total = []
    for i in ac_cables:
        counter_ac_cable += 1
        ac_cable_list = []
        ac_cable_list.append(i.ac_cables_number_id)
        ac_cables_data = ac_cable.objects.get(id=i.ac_cables_number_id)
        ac_cable_list.append(ac_cables_data.product_name)
        ac_cable_list.append(ac_cables_data.type)
        ac_cable_list.append(i.quantity)
        ac_cable_list.append(i.id)
        ac_cable_list_total.append(ac_cable_list)
    counter_dc_cable = 0
    dc_cable_list_total = []
    for i in dc_cables:
        counter_dc_cable += 1
        dc_cable_list = []
        dc_cable_list.append(i.dc_cables_number_id)
        dc_cables_data = dc_cable.objects.get(id=i.dc_cables_number_id)
        dc_cable_list.append(dc_cables_data.product_name)
        dc_cable_list.append(dc_cables_data.type)
        dc_cable_list.append(i.quantity)
        dc_cable_list.append(i.id)
        dc_cable_list_total.append(dc_cable_list)
    counter_others = 0
    others_list_total = []
    for i in other:
        counter_others += 1
        others_list = []
        others_list.append(i.others_number_id)
        others_data = others.objects.get(id=i.others_number_id)
        others_list.append(others_data.product_name)
        others_list.append(others_data.brand)
        others_list.append(i.quantity)
        others_list.append(i.id)
        others_list_total.append(others_list)


    return render(request, 'Procurement/procurement_part/project_detail.html', {'project':projects,'counter_inverters':counter_inversores,'inverters_list':inverters_list_total,
                                                                                'counter_modulos':counter_pv_modulos,'pv_modules_list':pv_modulos_list_total,
                                                                                'counter_construction':counter_construction,'construction_list':construction_list_total,
                                                                                'counter_structures':counter_structures,'structures_list':structures_list_total,
                                                                                'counter_inv_acessories':counter_inv_acessories,'inv_acessories_list':inv_acessorie_list_total,
                                                                                'counter_ac_cable':counter_ac_cable,'ac_cable_list':ac_cable_list_total,
                                                                                'counter_dc_cable':counter_dc_cable,'dc_cable_list':dc_cable_list_total,
                                                                                'counter_others':counter_others,'others_list':others_list_total})

#PDF Generation

@login_required(login_url='/login')
def venue_pdf(request,pk):
    projects = project.objects.get(id=pk)
    inverter = projects.order_inverter.all()
    pv_modulos = projects.order_pv_modules.all()
    constructions = projects.order_construction.all()
    structure = projects.order_structures.all()
    inverter_acessorie = projects.order_inverter_acessories.all()
    ac_cables = projects.order_ac_cables.all()
    dc_cables = projects.order_dc_cables.all()
    other = projects.order_others.all()
    counter_inversores = 0
    inverters_list_total = []
    for i in inverter:
        inverters_list = []
        counter_inversores += 1
        inverters_list.append(i.inverter_number_id)
        inversor = inverters.objects.get(id=i.inverter_number_id)
        inverters_list.append(inversor.product_name)
        inverters_list.append(inversor.power)
        inverters_list.append(i.quantity)
        inverters_list.append(i.id)
        inverters_list_total.append(inverters_list)
    counter_pv_modulos = 0
    pv_modulos_list_total = []
    for i in pv_modulos:
        pv_modulos_list = []
        counter_pv_modulos += 1
        pv_modulos_list.append(i.pv_modules_number_id)
        modulo = pv_modules.objects.get(id=i.pv_modules_number_id)
        pv_modulos_list.append(modulo.product_name)
        pv_modulos_list.append(modulo.power_range)
        pv_modulos_list.append(i.quantity)
        pv_modulos_list.append(i.id)
        pv_modulos_list_total.append(pv_modulos_list)
    counter_construction = 0
    construction_list_total = []
    for i in constructions:
        construction_list = []
        counter_construction += 1
        construction_list.append(i.construction_number_id)
        constructions_data = construction.objects.get(id=i.construction_number_id)
        construction_list.append(constructions_data.product_name)
        construction_list.append(constructions_data.brand)
        construction_list.append(i.quantity)
        construction_list.append(i.id)
        construction_list_total.append(construction_list)
    counter_structures = 0
    structures_list_total = []
    for i in structure:
        counter_structures += 1
        structures_list = []
        structures_list.append(i.structures_number_id)
        structures_data = structures.objects.get(id=i.structures_number_id)
        structures_list.append(structures_data.product_name)
        structures_list.append(structures_data.type)
        structures_list.append(i.quantity)
        structures_list.append(i.id)
        structures_list_total.append(structures_list)
    counter_inv_acessories = 0
    inv_acessorie_list_total = []
    for i in inverter_acessorie:
        counter_inv_acessories += 1
        inv_acessorie_list = []
        inv_acessorie_list.append(i.inverter_acessories_number_id)
        inv_acessorie_data = inverter_acessories.objects.get(id=i.inverter_acessories_number_id)
        inv_acessorie_list.append(inv_acessorie_data.product_name)
        inv_acessorie_list.append(inv_acessorie_data.type)
        inv_acessorie_list.append(i.quantity)
        inv_acessorie_list.append(i.id)
        inv_acessorie_list_total.append(inv_acessorie_list)
    counter_ac_cable = 0
    ac_cable_list_total = []
    for i in ac_cables:
        counter_ac_cable += 1
        ac_cable_list = []
        ac_cable_list.append(i.ac_cables_number_id)
        ac_cables_data = ac_cable.objects.get(id=i.ac_cables_number_id)
        ac_cable_list.append(ac_cables_data.product_name)
        ac_cable_list.append(ac_cables_data.type)
        ac_cable_list.append(i.quantity)
        ac_cable_list.append(i.id)
        ac_cable_list_total.append(ac_cable_list)
    counter_dc_cable = 0
    dc_cable_list_total = []
    for i in dc_cables:
        counter_dc_cable += 1
        dc_cable_list = []
        dc_cable_list.append(i.dc_cables_number_id)
        dc_cables_data = dc_cable.objects.get(id=i.dc_cables_number_id)
        dc_cable_list.append(dc_cables_data.product_name)
        dc_cable_list.append(dc_cables_data.type)
        dc_cable_list.append(i.quantity)
        dc_cable_list.append(i.id)
        dc_cable_list_total.append(dc_cable_list)
    counter_others = 0
    others_list_total = []
    for i in other:
        counter_others += 1
        others_list = []
        others_list.append(i.others_number_id)
        others_data = others.objects.get(id=i.others_number_id)
        others_list.append(others_data.product_name)
        others_list.append(others_data.brand)
        others_list.append(i.quantity)
        others_list.append(i.id)
        others_list_total.append(others_list)
    current_datetime = datetime.datetime.now()
    template=get_template('Procurement/pdf.html')
    html = template.render({'project':projects,'counter_inverters':counter_inversores,'inverters_list':inverters_list_total,'counter_modulos':counter_pv_modulos,'pv_modules_list':pv_modulos_list_total,
                                                                                'counter_construction':counter_construction,'construction_list':construction_list_total,
                                                                                'counter_structures':counter_structures,'structures_list':structures_list_total,
                                                                                'counter_inv_acessories':counter_inv_acessories,'inv_acessories_list':inv_acessorie_list_total,
                                                                                'counter_ac_cable':counter_ac_cable,'ac_cable_list':ac_cable_list_total,
                                                                                'counter_dc_cable':counter_dc_cable,'dc_cable_list':dc_cable_list_total,
                                                                                'counter_others':counter_others,'others_list':others_list_total,'current_datetime':current_datetime
                                                                                })
    result = BytesIO()
    #pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result,'attachment; filename="report.pdf"')
    #if not pdf.err:
     #   return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



@login_required(login_url='/login')
def inverter_detail(request,pk):
    new_order=None
    inverter = inverters.objects.get(id=pk)
    if request.method == 'POST':
        inverter_form=number_form_inverter(data=request.POST)
        if inverter_form.is_valid():
            new_order = inverter_form.save(commit=False)
            new_order.inverter_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_inverter/')
    else:
        inverter_form=number_form_inverter()
    return render(request, 'Procurement/procurement_part/inverter_detail.html', {'inverter':inverter,'form':inverter_form})

@login_required(login_url='/login')
def add_inverter(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_inverter=order_inverter1.objects.get(id=new_order)
        projeto_teste.order_inverter.add(order_inverter)
        return redirect('/inverters')

    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})


@login_required(login_url='/login')
def inverter_acessories_detail(request,pk):
    new_order=None
    inverter_acessorie = inverter_acessories.objects.get(id=pk)
    if request.method == 'POST':
        inverter_acessories_form=number_form_inverter_acessories(data=request.POST)
        if inverter_acessories_form.is_valid():
            new_order = inverter_acessories_form.save(commit=False)
            new_order.inverter_acessories_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_inverter_acessories/')
    else:
        inverter_acessories_form=number_form_inverter_acessories()
    return render(request, 'Procurement/procurement_part/inverter_acessories_detail.html', {'inverter_acessories':inverter_acessorie,'form':inverter_acessories_form})

@login_required(login_url='/login')
def add_inverter_acessories(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_inverter=order_inverter_acessories.objects.get(id=new_order)
        projeto_teste.order_inverter_acessories.add(order_inverter)
        return redirect('/inverter_acessories')

    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})

@login_required(login_url='/login')
def pv_modules_detail(request,pk):
    new_order = None
    pv_module = pv_modules.objects.get(id=pk)
    if request.method == 'POST':
        pv_module_form=number_form_pv_modules(data=request.POST)
        if pv_module_form.is_valid():
            new_order = pv_module_form.save(commit=False)
            new_order.pv_modules_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_pv_module/')
    else:
        pv_module_form=number_form_pv_modules()
    return render(request, 'Procurement/procurement_part/pv_module_detail.html', {'pv_module':pv_module,'form':pv_module_form})

@login_required(login_url='/login')
def add_pv_module(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_pv_module=order_pv_modules.objects.get(id=new_order)
        projeto_teste.order_pv_modules.add(order_pv_module)
        return redirect('/pv_modules')
    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})


@login_required(login_url='/login')
def construction_detail(request,pk):
    new_order = None
    constructions = construction.objects.get(id=pk)
    if request.method == 'POST':
        constructions_form=number_form_construction(data=request.POST)
        if constructions_form.is_valid():
            new_order = constructions_form.save(commit=False)
            new_order.construction_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_construction/')
    else:
        constructions_form=number_form_construction()
    return render(request, 'Procurement/procurement_part/construction_detail.html', {'construction':constructions,'form':constructions_form})

@login_required(login_url='/login')
def add_construction(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_constructions=order_construction.objects.get(id=new_order)
        projeto_teste.order_construction.add(order_constructions)
        return redirect('/construction')
    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})


@login_required(login_url='/login')
def structure_detail(request,pk):
    new_order = None
    structure = structures.objects.get(id=pk)
    if request.method == 'POST':
        structures_form=number_form_structures(data=request.POST)
        if structures_form.is_valid():
            new_order = structures_form.save(commit=False)
            new_order.structures_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_structures/')
    else:
        structures_form=number_form_structures()
    return render(request, 'Procurement/procurement_part/structures_detail.html', {'structure':structure,'form':structures_form})

@login_required(login_url='/login')
def add_structure(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_structure=order_structures.objects.get(id=new_order)
        projeto_teste.order_structures.add(order_structure)
        return redirect('/structures')
    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})


@login_required(login_url='/login')
def ac_cable_detail(request,pk):
    new_order = None
    ac_cables = ac_cable.objects.get(id=pk)
    if request.method == 'POST':
        ac_cables_form=number_form_ac_cables(data=request.POST)
        if ac_cables_form.is_valid():
            new_order = ac_cables_form.save(commit=False)
            new_order.ac_cables_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_ac_cables/')
    else:
        ac_cables_form=number_form_ac_cables()
    return render(request, 'Procurement/procurement_part/ac_cables_detail.html', {'ac_cable':ac_cables,'form':ac_cables_form})

@login_required(login_url='/login')
def add_ac_cable(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_ac_cable=order_ac_cables.objects.get(id=new_order)
        projeto_teste.order_ac_cables.add(order_ac_cable)
        return redirect('/ac_cables')
    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})

@login_required(login_url='/login')
def dc_cable_detail(request,pk):
    new_order = None
    dc_cables = dc_cable.objects.get(id=pk)
    if request.method == 'POST':
        dc_cables_form=number_form_dc_cables(data=request.POST)
        if dc_cables_form.is_valid():
            new_order = dc_cables_form.save(commit=False)
            new_order.dc_cables_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_dc_cables/')
    else:
        dc_cables_form=number_form_dc_cables()
    return render(request, 'Procurement/procurement_part/dc_cables_detail.html', {'dc_cable':dc_cables,'form':dc_cables_form})

@login_required(login_url='/login')
def add_dc_cable(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_dc_cable=order_dc_cables.objects.get(id=new_order)
        projeto_teste.order_dc_cables.add(order_dc_cable)
        return redirect('/dc_cables')
    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})

@login_required(login_url='/login')
def other_detail(request,pk):
    new_order = None
    other = others.objects.get(id=pk)
    if request.method == 'POST':
        others_form=number_form_others(data=request.POST)
        if others_form.is_valid():
            new_order = others_form.save(commit=False)
            new_order.others_number_id=pk
            new_order.save()
            request.session['data'] = new_order.id
            return redirect('add_others/')
    else:
        others_form=number_form_others()
    return render(request, 'Procurement/procurement_part/others_detail.html', {'others':other,'form':others_form})

@login_required(login_url='/login')
def add_others(request,pk):
    new_order = request.session.get('data')
    projetos=project.objects.all()
    if request.method == 'POST':
        valor=request.POST.get('project_value')
        projeto_teste=project.objects.get(id=valor)
        order_other=order_others.objects.get(id=new_order)
        projeto_teste.order_others.add(order_other)
        return redirect('/others')
    return render(request, 'Procurement/procurement_part/add_inverter.html',{'projects':projetos})

@login_required(login_url='/login')
def update_order_inverter(request,pk,py):
    order_inverters1=order_inverter1.objects.get(id=py)
    form = number_form_inverter(instance=order_inverters1)
    if request.method == 'POST':
        projects_form=number_form_inverter(data=request.POST,instance=order_inverters1)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_module(request,pk,py):
    order_module=order_pv_modules.objects.get(id=py)
    form = number_form_pv_modules(instance=order_module)
    if request.method == 'POST':
        projects_form=number_form_pv_modules(data=request.POST,instance=order_module)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_structure(request,pk,py):
    order_structure=order_structures.objects.get(id=py)
    form = number_form_structures(instance=order_structure)
    if request.method == 'POST':
        projects_form=number_form_structures(data=request.POST,instance=order_structure)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_construction(request,pk,py):
    order_constructions=order_construction.objects.get(id=py)
    form = number_form_construction(instance=order_constructions)
    if request.method == 'POST':
        projects_form=number_form_construction(data=request.POST,instance=order_constructions)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_inv_acessorie(request,pk,py):
    order_inverter_acessorie=order_inverter_acessories.objects.get(id=py)
    form = number_form_inverter_acessories(instance=order_inverter_acessorie)
    if request.method == 'POST':
        projects_form=number_form_inverter_acessories(data=request.POST,instance=order_inverter_acessorie)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_ac_cables(request,pk,py):
    order_ac_cable=order_ac_cables.objects.get(id=py)
    form = number_form_ac_cables(instance=order_ac_cable)
    if request.method == 'POST':
        projects_form=number_form_ac_cables(data=request.POST,instance=order_ac_cable)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_dc_cables(request,pk,py):
    order_dc_cable=order_dc_cables.objects.get(id=py)
    form = number_form_dc_cables(instance=order_dc_cable)
    if request.method == 'POST':
        projects_form=number_form_dc_cables(data=request.POST,instance=order_dc_cable)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def update_order_other(request,pk,py):
    order_other=order_others.objects.get(id=py)
    form = number_form_others(instance=order_other)
    if request.method == 'POST':
        projects_form=number_form_others(data=request.POST,instance=order_other)
        if projects_form.is_valid():
            new_project=projects_form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect ('/projects/'+pk,{'message':'Project Saved'})
    guardar='Update Order'
    context = {'form':form,'name_save':guardar}
    return render(request, 'Procurement/procurement_part/creation.html',context)

@login_required(login_url='/login')
def delete_order_inverter (request,pk,py):
    order_inverter = order_inverter1.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_inverter.delete()
        return redirect(next)
    context = {'item':order_inverter,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_pv_module (request,pk,py):
    order_module = order_pv_modules.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_module.delete()
        return redirect(next)
    context = {'item':order_module,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_construction (request,pk,py):
    order_constructions = order_construction.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_constructions.delete()
        return redirect(next)
    context = {'item':order_constructions,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_structures (request,pk,py):
    order_structure = order_structures.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_structure.delete()
        return redirect(next)
    context = {'item':order_structure,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_inv_acessorie (request,pk,py):
    order_inverter_acessorie = order_inverter_acessories.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_inverter_acessorie.delete()
        return redirect(next)
    context = {'item':order_inverter_acessorie,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_ac_cables (request,pk,py):
    order_ac_cable = order_ac_cables.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_ac_cable.delete()
        return redirect(next)
    context = {'item':order_ac_cable,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_dc_cables (request,pk,py):
    order_dc_cable = order_dc_cables.objects.get(id=py)
    next = '/procurement/projects/'+pk
    if request.method=="POST":
        order_dc_cable.delete()
        return redirect(next)
    context = {'item':order_dc_cable,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

@login_required(login_url='/login')
def delete_order_other (request,pk,py):
    order_other = order_others.objects.get(id=py)
    next = '/projects/'+pk
    if request.method=="POST":
        order_other.delete()
        return redirect(next)
    context = {'item':order_other,'next':next}
    return render(request,'Procurement/procurement_part/delete.html',context)

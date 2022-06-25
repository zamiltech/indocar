from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _, ugettext
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.models import User


from .models import Offer,Offer_line,Services,Places,Price_Plan,Company

from .forms import OfferForm
# Create your views here.

#@login_required(login_url='index')
def editoffer(request,offer_id):
    x=request.GET.get('offer_id')
    main_offer = Offer.objects.get(local_id=offer_id)
    main_offer_id= main_offer.Offer_id
    main_Services = Services.objects.all()
    main_Places = Places.objects.all()
    offer_lines = Offer_line.objects.filter(offer_id=main_offer)

    main_offer_pax = main_offer.Numbers_of_Pax
    
    context = {
        'main_offer_id' : main_offer_id,
        'main_offer_pax' : main_offer_pax ,
        'main_offer' : main_offer,
        'main_Services' : main_Services ,
        'main_Places' : main_Places ,
        'offer_id' : offer_id ,
        'offer_lines' : offer_lines,
    }
    return render(request, 'addoffer.html',  context=context)

@login_required(login_url='login')
def showofferlist(request):

    main_offer = Offer.objects.all()
    main_Services = Services.objects.all()
    main_Places = Places.objects.all()

    
    context = {


        'main_offer' : main_offer,
        'main_Services' : main_Services ,
        'main_Places' : main_Places ,


    }
    return render(request, 'offerlist.html',  context=context)

def getserviceprice(request):
    price = -1
    try:
        _pax = request.GET.get('pax')
        _service = request.GET.get('service')
        _place = request.GET.get('place')
        main_Price_Plan = Price_Plan.objects.filter(Numbers_of_Pax__gte=_pax,Service=_service,Location=_place).order_by('Numbers_of_Pax')[:1].get()
        sys_price = main_Price_Plan.Price
        return HttpResponse(sys_price)
    except :
        return HttpResponse("-1")   

@login_required(login_url='login')
def updateoffercost(offerid):
    main_offer = Offer.objects.get(Offer_id=offerid)
    x_price= 0
    for _o_line in Offer_line.objects.filter(offer_id=main_offer):
         x_price =x_price + _o_line.Price

    main_offer.Total_Price = x_price
    main_offer.save()

def deletewofferline(request):
    main_main_offer = request.GET.get('offer_id')
    local_offer_line_id = request.GET.get('offer_line_local_id')
    print (local_offer_line_id)
    _line_offer = Offer_line.objects.filter(line_local_id=local_offer_line_id).get()
    _line_offer.delete()
    updateoffercost(main_main_offer) 

    return HttpResponse("Ok")

@login_required(login_url='login')
def addnewofferline(request):

    #try:
    main_main_offer = request.GET.get('offer_id')
    main_offer = Offer.objects.get(Offer_id=main_main_offer)
    _numbers_of_pax = request.GET.get('pax')
    #_place = request.GET.get('place')
    _service = Services.objects.filter(pk=request.GET.get('service')).get()
    _location = Places.objects.filter(pk=request.GET.get('place')).get()
    _price = request.GET.get('price')
    #print (_price)
    C_Offer_line = Offer_line()
    C_Offer_line.offer_id=main_offer
    C_Offer_line.Numbers_of_Pax=_numbers_of_pax
    C_Offer_line.Service=_service
    C_Offer_line.Location=_location
    ## Get the price again
    main_Price_Plan = Price_Plan.objects.filter(Numbers_of_Pax__gte=_numbers_of_pax,Service=_service,Location=_location).order_by('Numbers_of_Pax')[:1].get()
    C_Offer_line.Price = main_Price_Plan.Price
    C_Offer_line.Line_Notes = main_Price_Plan.Notes
    C_Offer_line.save()
    updateoffercost(main_main_offer)
    #print (C_Offer_line.pk)
    #C_Offer_line_Save=C_Offer_line.objects.get(Offer_line_id=C_Offer_line.pk)


    return HttpResponse(C_Offer_line.line_local_id)
    #except :
       # return HttpResponse("-1")            

@login_required(login_url='login')
def newoffer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            
            # Create Master company profile
            #_offer = form.save(commit=False)
            _offer = Offer ()
            _offer.Numbers_of_Pax = form.cleaned_data.get('Numbers_of_Pax')
            _offer.Company_name = Company.objects.filter(users=request.user)[:1].get()
            _offer.Offer_user = request.user
            _offer.save()

            #co_master.co_master_name = form.cleaned_data.get('co_name')   
            
            #form.save()
            

            return redirect('edit-offer', _offer.local_id)
    else:
        form = OfferForm()
    return render(request, 'newoffer.html', {'form': form})       
from django.urls import path, include, reverse
from django.conf.urls.i18n import i18n_patterns
#from .views import ActivateLanguageView
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('offer/update/<uuid:offer_id>/', views.editoffer, name='edit-offer'),
    path('getserviceprice', views.getserviceprice, name='getserviceprice'),
    path('ajxsaveofferline', views.addnewofferline, name='ajxsaveofferline'),
    path('ajxdelofferline', views.deletewofferline, name='ajxdelofferline'),
    path('ajxcloseoffer', views.closeoffer, name='ajxcloseoffer'),
    path('offer/list', views.showofferlist, name='showofferlist'),
    path('', views.showofferlist, name='showofferlist'),
    path('offer/new', views.newoffer, name='newoffer'),
    path('accounts/', include('django.contrib.auth.urls')),   
]

from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.auth.models import User

from django import forms
from .models import Offer,Company


# creating a form
class OfferForm(forms.ModelForm):
    #Company_name = forms.ModelChoiceField(queryset=Company.objects.all(),empty_label=None, label=_(u'Company'))
    Numbers_of_Pax  = forms.IntegerField(label=_(u'Numbers of Pax'))

    class Meta:
        model = Offer
        fields = ('Numbers_of_Pax',)#'Company_name')

    #def __init__(self, user, *args, **kwargs):
        #super(OfferForm, self).__init__(*args, **kwargs)
        ### Filter the company list ####
        #self.fields['Company_name'].queryset = Company.objects.filter(users__in=user)
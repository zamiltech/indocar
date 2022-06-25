from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.auth.models import User
from django.utils import timezone

import uuid

class Services(models.Model):
    Service_name = models.CharField(_(u'Service name'), unique=True, max_length=100,default="")

    def __str__(self):
        return f'{self.Service_name} '
    class Meta:
        verbose_name = _(u'Services')
        verbose_name_plural = _('Services')

class Places(models.Model):
    Place_name = models.CharField(_(u'Place name'), unique=True, max_length=200,default="")

    def __str__(self):
        return f'{self.Place_name} '
    class Meta:
        verbose_name = _(u'Places')
        verbose_name_plural = _('Places')

class Price_Plan(models.Model):
    Numbers_of_Pax = models.PositiveSmallIntegerField(_(u'Numbers of Pax'),default=1)
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)
    Location = models.ForeignKey(Places, on_delete=models.CASCADE)
    Price = models.PositiveSmallIntegerField(_(u'Price'))
    Notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.Numbers_of_Pax} :: {self.Service} - {self.Location} '

    class Meta:
        verbose_name = _(u'Price Plan')
        verbose_name_plural = _('Price Plan')

class Company(models.Model):
    Company_name = models.CharField(_(u'Company name'), unique=True, max_length=200,default="")
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.Company_name} '
    class Meta:
        verbose_name = _(u'Company')
        verbose_name_plural = _('Company')

class Offer(models.Model):
    Offer_id = models.AutoField(primary_key=True)
    local_id = models.UUIDField(default=uuid.uuid4, unique=True)#, editable=False)
    Numbers_of_Pax = models.PositiveSmallIntegerField(_(u'Numbers of Pax'),default=2)
    Company_name = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True,null=True)
    Offer_user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    Total_Price = models.PositiveSmallIntegerField(_(u'Total Price'),default=0)
    create_date = models.DateTimeField(_(u'Created Date'), default=timezone.now, editable=False)
    is_closed = models.BooleanField(_(u'Is Closed?'),default=False)
    

    def __str__(self):
        return f'{self.Offer_id} - {self.Company_name} '
    class Meta:
        verbose_name = _(u'Offer')
        verbose_name_plural = _('Offer')

class Offer_line(models.Model):
    Offer_line_id = models.AutoField(primary_key=True)
    line_local_id = models.UUIDField(default=uuid.uuid4, unique=True)#, editable=False)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)
    Numbers_of_Pax = models.PositiveSmallIntegerField(_(u'Numbers of Pax'),default=2)
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)
    Location = models.ForeignKey(Places, on_delete=models.CASCADE)
    Price = models.PositiveSmallIntegerField(_(u'Price'))
    Line_Notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.offer_id} - {self.Offer_line_id} - {self.Service} - {self.Location} '
    class Meta:
        verbose_name = _(u'Offer Lines')
        verbose_name_plural = _('Offer Lines')
from django.contrib import admin

# Register your models here.
from .models import Services,Places,Price_Plan,Company,Offer,Offer_line

@admin.register(Services)
class Services_Admin(admin.ModelAdmin):
    pass


@admin.register(Places)
class Places_Admin(admin.ModelAdmin):
    pass

@admin.register(Price_Plan)
class Price_Plan_Admin(admin.ModelAdmin):
    pass

@admin.register(Company)
class Company_Admin(admin.ModelAdmin):
    pass

@admin.register(Offer)
class Offer_Admin(admin.ModelAdmin):
    pass

@admin.register(Offer_line)
class Offer_line_Admin(admin.ModelAdmin):
    pass
from django.contrib import admin
from contact.models import  Contact

class ContactAdmin(admin.ModelAdmin):
    list_display =('full_name','subject','email','company_name','message','date')
admin.site.register(Contact,ContactAdmin)

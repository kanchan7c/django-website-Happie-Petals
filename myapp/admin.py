from django.contrib import admin
from myapp.models import Contact, Register, Custom

# Register your models here.
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Custom)
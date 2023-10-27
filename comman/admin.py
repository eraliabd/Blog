from django.contrib import admin
from .models import ContactInfo, ContactRequest, About


admin.site.register(ContactInfo)
admin.site.register(ContactRequest)
admin.site.register(About)

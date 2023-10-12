from django.contrib import admin

from hos.models import User, Diagnose, Patient

#registring models in the admin panel:
admin.site.register(User)
admin.site.register(Diagnose)
admin.site.register(Patient)

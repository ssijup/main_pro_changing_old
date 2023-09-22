from django.contrib import admin
from .models import LawFirm,LawfirmAdmin, AdvocateLawfirmInvitation



admin.site.register(LawFirm)
admin.site.register(LawfirmAdmin)
admin.site.register(AdvocateLawfirmInvitation)
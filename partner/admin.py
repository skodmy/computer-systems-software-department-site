from django.contrib import admin
from .models import Partner


class PartnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partner, PartnerAdmin)

from django.contrib import admin

from .models import Fact


class FactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fact, FactAdmin)

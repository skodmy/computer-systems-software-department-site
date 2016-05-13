from django.contrib import admin

from .models import Fact, FactArgument, ArgumentType


class FactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fact, FactAdmin)
admin.site.register(FactArgument)
admin.site.register(ArgumentType)

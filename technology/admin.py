from django.contrib import admin

from .models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Technology, TechnologyAdmin)

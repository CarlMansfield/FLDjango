from django.contrib import admin
from .models import Nation


class NationAdmin(admin.ModelAdmin):
    list_display = ['country']


admin.site.register(Nation, NationAdmin)

# Register your models here.

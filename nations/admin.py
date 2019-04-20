from django.contrib import admin
from .models import Nation, League


class NationAdmin(admin.ModelAdmin):
    list_display = ['country']


class NationLeague(admin.ModelAdmin):
    list_display = ['lName']


admin.site.register(Nation, NationAdmin)
admin.site.register(League, NationLeague)

# Register your models here.

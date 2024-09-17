from django.contrib import admin
from api.models import Authors


@admin.register(Authors)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name',)
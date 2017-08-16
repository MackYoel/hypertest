from django.contrib import admin
from .models import Theme, Duel


class DuelAdmin(admin.ModelAdmin):
    list_display = ('token', 'pk')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Duel, DuelAdmin)

from django.contrib import admin

from .models import Hero


class HeroAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hero, HeroAdmin)

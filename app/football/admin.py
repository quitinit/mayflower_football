from django.contrib import admin

from football.models import Player,Team,Match,Location

# Register your models here.

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Location)
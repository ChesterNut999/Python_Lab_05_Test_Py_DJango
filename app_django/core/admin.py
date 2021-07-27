from django.contrib import admin
from core.models import Pessoas

# Register your models here.
pessoas = Pessoas.objects.get(nome='Maurilio')

class PessoasAdmin(admin.ModelAdmin):
    list_display = ('nome','idade')
    list_filter = ('nome',)

admin.site.register(Pessoas)

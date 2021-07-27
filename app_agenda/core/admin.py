from django.contrib import admin
from core.models import Eventos

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'usuario', 'data_criacao', 'data_evento', 'local')
    list_filter = ('usuario',)

admin.site.register(Eventos, EventosAdmin)
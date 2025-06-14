from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipo

admin.site.register(EquipoFutbol)
admin.site.register(Jugador)
admin.site.register(Campeonato)
admin.site.register(CampeonatoEquipo)
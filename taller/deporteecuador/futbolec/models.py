from django.db import models

# Create your models here.

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10, unique=True)
    twitter = models.CharField("username twitter", max_length=50)

    def __str__(self):
        return "Equipo: %s (%s) - Twitter: @%s" % (self.nombre, self.siglas, self.twitter)


class Jugador(models.Model):
    opciones_posicion = (
        ('arquero', 'Arquero'),
        ('defensa', 'Defensa'),
        ('mediocampo', 'Mediocampo'),
        ('delantero', 'Delantero'),
    )

    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=20, choices=opciones_posicion)
    numero_camiseta = models.IntegerField("número de camiseta")
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return "Jugador: %s - Posición: %s - Camiseta #%d - Sueldo: $%.2f - Equipo: %s" % (
            self.nombre,
            self.posicion,
            self.numero_camiseta,
            self.sueldo,
            self.equipo.nombre
        )


class Campeonato(models.Model):
    nombre = models.CharField("nombre del campeonato", max_length=100)
    auspiciante = models.CharField("nombre del auspiciante", max_length=100)

    def __str__(self):
        return "Campeonato: %s - Auspiciado por: %s" % (self.nombre, self.auspiciante)


class CampeonatoEquipo(models.Model):
    anio = models.IntegerField("año")
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return "Año: %d - Equipo: %s - Campeonato: %s" % (
            self.anio,
            self.equipo.nombre,
            self.campeonato.nombre
        )

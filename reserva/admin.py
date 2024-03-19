from django.contrib import admin
from reserva.models import Reserva
# Register your models here.


@admin.register(Reserva)
class Reservaadmin(admin.ModelAdmin):
    list_display = ['nomeDoPet','nomeDoDono', 'dia','turno']
    search_fields =['nomdeDoPet', 'nomeDoDono']
    list_filter = ['dia','turno','tamanho']
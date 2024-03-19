from django.urls import path
from reserva.views import reserva 


app_name = 'reserva'

urlpatterns = [
    path ('criar/', reserva, name='criar_reserva')


        ]       


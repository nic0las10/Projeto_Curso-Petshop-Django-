from typing import Any
from django.core.management.base import BaseCommand

from model_bakery import baker

from reserva.models import Reserva 

class Command(BaseCommand):
    help = 'Criar dados fake para testar api de Agendamento '

    def handle(self, *args,  **options ):
        total = 100
        

        self.stdout.write(
            self.style.HTTP_INFO(f'Criando {total} agendamentos')

        )

        for i in range(total):
            self.stdout.write(
                self.style.HTTP_INFO(f'Criando reserva númerp {i + 1}') 

            )
            
            reserva = baker.make(Reserva)
            reserva.save()

        self.stdout.write(
            self.style.SUCCESS('Agendamentos Criados com sucesso!')

        )


        

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Cria um novo arquivo para um usuario passado por paramentro'



    def add_arguments(self, parser ):
        parser.add_argument('--username',required = True) 
        parser.add_argument('--password', required = True)

    def handle(self, *args, **options):
        username = options ['username']
        password = options['password']
        

        self.stdout.write(
            self.style.WARNING(f'Criando usuario com nome {username}')
        )

        user = User(username=username)
        user.first_name = username
        user.set_password(password)
        user.save()

        self.stdout.write(
         self.style.SUCCESS('Usuário criado com sucesso!'))

        self.stdout.write(
         self.style.HTTP_INFO('Criando token para este usuário!'))

        token = Token.objects.create(user=user)
        
        self.stdout.write(
         self.style.SUCCESS(f'token gerado:{token.key}'))



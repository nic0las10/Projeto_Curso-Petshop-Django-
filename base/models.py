from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email= models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.TimeField(auto_now_add = True)
    lido = models.BooleanField(blank=True, default=False)


    def __str__(self):
        return f'Nome: {self.nome} - Email: {self.email}'



    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering =['nome']


class Reserva(models.Model):
    nomeDoPet = models.CharField(max_length=50, verbose_name="Nome do Pet")
    Telefone = models.CharField(max_length=15)
    Dia = models.DateField(verbose_name = 'Dia da Reserva')
    observaçoes = models.TextField(verbose_name = "Observações")
    
from django.db import models

# Create your models here.
class Reserva(models.Model):
    TAMANHO_OPCOES = (
        (0,'Pequeno'),
        (1,'Médio'),
        (2,'Grande')
    )
    TURNO_OPCOES =(
        ('manha','Manhã'),
        ('tarde','Tarde'),
        
    )
    nomeDoPet = models.CharField(max_length=50, verbose_name="Nome do Pet")
    nomeDoDono = models.CharField(max_length=80, verbose_name="Nome do Dono")
    telefone = models.CharField(max_length = 15)
    dia = models.DateField(verbose_name = 'Dia da Reserva')
    observaçoes = models.TextField(verbose_name = "Observações")
    tamanho = models.IntegerField(verbose_name = 'Tamanho', choices = TAMANHO_OPCOES )
    turno = models.CharField(verbose_name ='Turno', choices = TURNO_OPCOES, max_length = 5)
    petshop = models.ForeignKey(
         'Petshop',
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    




class Petshop(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50 )
    rua = models.CharField(verbose_name="Rua", max_length=100)
    numero = models.CharField(verbose_name= "Número", max_length=10)
    bairro = models.CharField(verbose_name="Bairro", max_length=50)


    
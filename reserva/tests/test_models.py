import pytest
from reserva.models  import Reserva, Petshop
from model_bakery import baker
from datetime import date


def test_config():
    assert 1 == 1

@pytest.fixture
def reserva():
      dia = date(2024,4,25)
      reserva = baker.make(
        Reserva ,
        nomeDoPet = 'budy',
        dia = dia,
        turno ='manha'
    )
      return reserva
      



@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
     assert str(reserva) == 'Nome do PET: budy - Dia de reserva:2024-04-25 - Turno: manha'


@pytest.mark.django_db
def test_quantidade_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 5 
    baker.make(
        Reserva,
        quantidade,
        petshop = petshop
    )

    assert petshop.qtd_reservas() == 5 
import pytest
from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta


def test_reserva_view_retornar_template_correto(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200 
    assertTemplateUsed(response, 'reserva_de_banho.html')



@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client):
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nomeDoPet': 'Lua',
        'nomeDoDono':'Nicolas',
        'telefone': '54 999999447',
        'dia':amanha,
        'observacoes': 'sujo',
        'tamanho': 0,
        'turno': 'tarde'

    }


    response = client.post('/reserva/criar/', dados)

    assert response.status_code == 200
    assert 'Agendamento feito com Sucesso!' in str(response.content
    )






















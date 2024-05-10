from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from rest_api.serializers import AgendamentoModelSerializer, PetshopModelSerializer

from reserva.models import Reserva, Petshop




class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]





@api_view(['GET', 'POST'])
def hello_word (request):
    if request.method == 'POST':
        nomeRecebido = request.data.get('nome')
        idadeRecebida = request.data.get('idade')
        return Response({"message": f'Olá {nomeRecebido}, Você tem {idadeRecebida} anos '})
    
    return Response({'message': 'Hello Word!'})


    

# Create your views here.


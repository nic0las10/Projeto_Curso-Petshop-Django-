from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField

from reserva.models import Reserva, Petshop

class PetshopNesteModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'


class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self,**kwargs):
        self.serializer = PetshopNesteModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
    queryset =Petshop.objects.all(),
    read_only = False)

    class Meta:
        model = Reserva
        fields = '__all__'

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'  # Substitua pelo nome correto da sua view de detalhes da reserva
    )

    class Meta:
        model = Petshop
        fields = '__all__'


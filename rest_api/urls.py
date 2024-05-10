from django.urls import path
from rest_api.views import hello_word, AgendamentoModelViewSet, PetshopModelViewSet
from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = [
    path('hello_word/', hello_word, name='hello_word_api'),
]

urlpatterns += router.urls

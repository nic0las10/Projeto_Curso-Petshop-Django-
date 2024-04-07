from django.urls import path
from rest_api.views import hello_word, AgendamentoModelViewSet
from rest_framework.routers import SimpleRouter

app_name ='rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)

urlpatterns = [
    path('hello_word', hello_word, name='hello_word_api')
]

urlpatterns +=  router.urls


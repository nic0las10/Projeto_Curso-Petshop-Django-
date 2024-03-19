from django.contrib import admin,messages

# Register your models here
from base.models import Contato

@admin.action(description='Marcar Formulário(s) como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulários de Contato(s) marcado(s) como lido', messages.SUCCESS)


@admin.action(description='Marcar Formulário(s) como não lido')
def marcar_como_nao_lido(modeladmin, request, queryset):
    queryset.update(lido=False)
    modeladmin.message_user(request, 'Formulários de Contato(s) marcado(s) como não lido', messages.SUCCESS)



@admin.register(Contato)
class Contatoadmin(admin.ModelAdmin):
    list_display = ['nome','email', 'mensagem', 'lido']
    search_fields = ['nome', 'email']
    list_filter = ['data','lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]

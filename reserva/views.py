from django.shortcuts import render
from reserva.forms import ReservaForm

# Create your views here.

def reserva(request):
    sucesso = False
    if request.method =='GET':
       form = ReservaForm()

    elif request.method =='POST':
      form = ReservaForm(request.POST)
      if form.is_valid():
         sucesso = True
         form.save()

       
   
    contexto = {
        'nome':' Nicolas de macedo',
        'telefone': '54999464972',
        'formulario': form,
        'sucesso': sucesso
        

    }

    return render (request, 'reserva_de_banho.html', contexto)
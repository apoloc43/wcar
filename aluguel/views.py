# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Carro, Aluguel,Cliente
from .forms import AluguelForm,CarroForm
from .admin import CustomUserCreationForm
from django.contrib import messages 


# Create your views here.

def index(request):
    carros = Carro.objects.all()[:5]
    return render(request, 'index.html', {"carros":carros})

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros":carros})

def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    return render(request, 'carro/detalhar.html', {"carro":carro})

@login_required 
@permission_required('aluguel.add_carro')
def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CarroForm()
            return render(request, "carro/cadastrar.html" , {'form': form})
    else:
        form = CarroForm()
        return render(request, "carro/cadastrar.html", {'form': form})

@login_required 
@permission_required('aluguel.edit_carro')
def atualizar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    form = CarroForm(instance=carro)
    
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "carro/atualizar.html", {'form': form})
    else:
        return render(request, "carro/atualizar.html", {'form': form})
    
@login_required
@permission_required('aluguel.delete_carro')    
def deletar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)

    if carro:
        carro.delete()
        return redirect("/")
    else:
        return render(request, "carro/listar.html", {'msg': "carro não encontrado"})

@login_required 
@permission_required('aluguel.view_carro')
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar.html', {"clientes":clientes})

@login_required 
def detalhar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'cliente/detalhar.html', {"cliente":cliente})

@login_required
@permission_required('aluguel.view_aluguel')  
def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'aluguel/listar.html', {"alugueis":alugueis})

    

@login_required 
def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/cadastrar.html", {'form': form})

@login_required 
def realizar_aluguel_carro(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)
    aluguel = Aluguel()
    aluguel.carro = carro
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})
    

def register(request):
        form = CustomUserCreationForm()
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
    
            if form.is_valid():
                user = form.save(commit=False)
                user.is_valid = False
                user.save()
                # messages.success(request, 'Registrado. Agora faça o login para começar!')
                return render(request,'index.html')

            else:
                print('invalid registration details')
                
        return render(request, "registration/register.html",{"form": form})
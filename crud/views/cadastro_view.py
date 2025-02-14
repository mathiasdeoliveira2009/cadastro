from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from crud.models.cadastro_model import CadastroModel
from crud.forms import CadastroForm
from django.contrib import messages

def CadastroView(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('listar_clientes')
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os campos.")
    else:
        form = CadastroForm()

    return render(request, 'crud/cadastro.html', {"form": form})

def listar_clientes(request):
    clientes = CadastroModel.objects.all().order_by('-id')
    return render(request, 'crud/index.html', {'terceiros': clientes})

def remover(request, terceiro_id):
    terceiro = get_object_or_404(CadastroModel, id=terceiro_id)
    terceiro.delete()
    messages.success(request, "Cliente removido com sucesso!")
    return redirect('listar_clientes')

def mudar(request, terceiro_id):
    terceiro = get_object_or_404(CadastroModel, id=terceiro_id)

    if request.method == "POST":
        form = CadastroForm(request.POST, instance=terceiro)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados alterados com sucesso!")
            return redirect('listar_clientes')
        else:
            messages.error(request, "Erro ao editar. Verifique os campos.")
    else:
        form = CadastroForm(instance=terceiro)

    return render(request, 'crud/mudar.html', {'form': form, 'terceiro': terceiro})

def cadastrar_terceiro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_clientes")  # Redireciona após o sucesso
        else:
            # Retorna o formulário preenchido com os erros
            return render(request, "crud/cadastro.html", {"form_terceiro": form})

    else:
        form = CadastroForm()
    return render(request, "crud/cadastro.html", {"form_terceiro": form})

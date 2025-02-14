from django.contrib import admin
from django.urls import path , include
from crud.views.cadastro_view import listar_clientes , CadastroView , remover , mudar
from crud.views.index_view import IndexView

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('remover/<int:terceiro_id>/', remover, name='remover'),
    path('mudar/<int:terceiro_id>/', mudar, name='mudar'),
    path('cadastrar/', CadastroView, name='cadastrar_cliente'),
]

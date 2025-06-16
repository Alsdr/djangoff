import django_filters
from escola.models import Client, Lista, TodoItem


class ClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cpf = django_filters.CharFilter(lookup_expr='exact')
    rg = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'cpf', 'rg']

class ListaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Lista
        fields = ['id', 'name']

class TodoItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    lista_id = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    ativo = django_filters.BooleanFilter(lookup_expr='icontains')
    prioridade = django_filters.BooleanFilter(lookup_expr='icontains')


    class Meta:
        model = TodoItem
        fields = ['id','lista_id', 'descricao', 'ativo', 'prioridade']

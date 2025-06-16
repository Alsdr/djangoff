from rest_framework import serializers

from escola.models import Client, Lista, TodoItem, Todo

class ClientSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=18, max_value=100)

    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'rg', 'cpf']


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ['id', 'name']

class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItem
        fields = '__all__'
        # fields = '__all__'
        # extra_kwargs = {
        #     'id_list': {'required': True}  # Força o campo a ser obrigatório
        # }


from rest_framework import serializers
from .models import Todo
from rest_framework.fields import DateTimeField


class TodoSerializer(serializers.ModelSerializer):
    created_at = DateTimeField(format='%Y-%m-%dT%H:%M:%S.%fZ', read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'text', 'done', 'created_at']
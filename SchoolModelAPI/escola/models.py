from django.db import models
from django.utils import timezone



class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        abstract = True
        managed = True
        # db_table = 'escola'


class Client(ModelBase):
    name = models.CharField(
        db_column='tx_nome',
        max_length=70,
        null=False
    )
    age = models.IntegerField(
        db_column='nb_idade',
        null=False
    )
    rg = models.CharField(
        db_column='tx_rg',
        max_length=12,
        null=False
    )
    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=12,
        null=False
    )

    def __str__(self):
        return f"{self.id} - {self.name}"

class Lista(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=70,
        null=False
    )

    def __str__(self):
        return f"{self.id} - {self.name}"


from django.db import models
from django.utils import timezone


class Todo(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']  # Ordenação padrão


class TodoItem(models.Model):
    # Campos básicos
    lista = models.ForeignKey(
        Lista,
        db_column='id_list',
        null=True,
        on_delete=models.DO_NOTHING
    )

    descricao = models.CharField(
        db_column='tx_descricao',
        max_length=200,
        null=False,
        verbose_name="Descrição",
        help_text="Detalhes da tarefa (até 200 caracteres)"
    )

    STATUS = [
        ('P', 'Pendente'),
        ('C', 'Concluído'),
    ]
    ativo = models.CharField(
        db_column='tx_status',
        max_length=1,
        choices=STATUS,
        default='P',
        verbose_name="Status"
    )
    PRIORIDADE_CHOICES = [
        (1, 'Prioridade 1 (Alta)'),
        (2, 'Prioridade 2 (Média)'),
        (3, 'Prioridade 3 (Baixa)'),
    ]

    prioridade = models.IntegerField(
        db_column='tx_prioridade',
        choices=PRIORIDADE_CHOICES,  # Restringe aos valores 1, 2, 3
        null=True,
        verbose_name="Prioridade",
        blank=True  # Permite campo vazio (opcional)
    )


    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.ativo} - {self.prioridade}"
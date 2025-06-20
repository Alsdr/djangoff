# Generated by Django 5.2.1 on 2025-06-13 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_lista_todoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='qtdItems',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='name',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='ativo',
            field=models.CharField(choices=[('P', 'Pendente'), ('C', 'Concluído')], db_column='tx_status', default='P', max_length=1, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='lista',
            field=models.ForeignKey(db_column='id_list', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='escola.lista'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='prioridade',
            field=models.IntegerField(blank=True, choices=[(1, 'Prioridade 1 (Alta)'), (2, 'Prioridade 2 (Média)'), (3, 'Prioridade 3 (Baixa)')], db_column='tx_prioridade', null=True, verbose_name='Prioridade'),
        ),
    ]

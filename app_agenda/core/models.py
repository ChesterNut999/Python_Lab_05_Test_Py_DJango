from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação do evento')
    local = models.TextField(blank=True, null=True, verbose_name='Local/Endereço')

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # é uma boa prática que o nome da tabela possua o mesmo nome da classe
        db_table = 'Eventos'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y - %H: %M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
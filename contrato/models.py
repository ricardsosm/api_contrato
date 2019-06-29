from django.db import models
from cliente.models import Cliente
from banco.models import Banco

class Contrato(models.Model):

	nome = models.CharField(null=True, blank=True,max_length=20)
	valor = models.FloatField(null=True, blank=True)
	parcelas = models.IntegerField()
	tx_juros = models.FloatField(null=True, blank=True)
	ip = models.GenericIPAddressField(null=True, blank=True)
	criando_em = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	atualizado_em = models.DateTimeField(
		'Atualizado em',auto_now=True
	)	
	id_banco = models.ForeignKey(Banco,on_delete=models.CASCADE)
	id_cliente =  models.ForeignKey(Cliente,on_delete=models.CASCADE)

	def __str__(self):
		return self.nome
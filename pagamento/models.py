from django.db import models
from contrato.models import Contrato

class Pagamento(models.Model):
	
	valor = models.FloatField(null=True, blank=True)
	parcela = models.IntegerField()
	criando_em = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	id_contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)
		

from django.db import models

class Banco(models.Model):

	nome = models.CharField('Nome',max_length=30)
	num_banco = models.IntegerField()	
	ag = models.CharField('Agencia',max_length=30)	

	def __str__(self):
		return self.nome	

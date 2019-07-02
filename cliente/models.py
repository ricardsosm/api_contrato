from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
				

	nome = models.CharField('Nome',max_length=30)	
	cpf = models.CharField(null=True, blank=True, unique=True,max_length=14)
	tel = models.CharField('Telefone',max_length=20,null=True, blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	user = models.ManyToManyField(User)


	def set(self,pk):
		self.id_usuario = pk
		return  True

	def __str__(self):
		return self.nome

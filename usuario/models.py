from django.db import models
from django.contrib.auth.models import UserManager

class Usuario(models.Model):
	
	username = models.CharField('Nome do Usuario', max_length=30,unique=True,default='')
	email = models.EmailField('Email',default='')
	is_active = models.BooleanField('Esta ativo',blank=True,default=True)
	is_staff = models.BooleanField('Master',blank=True,default=False)
	date_joined = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS =  ['email']

	def __str__(self):
		return self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		ordering = ['username']
from django.contrib import admin
from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
	
	list_display = ['nome','cpf']
	search_field = ['nome']

admin.site.register(Cliente,ClienteAdmin)

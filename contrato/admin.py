from django.contrib import admin
from contrato.models import Contrato

class ContratoAdmin(admin.ModelAdmin):
	
	list_display = ['valor','parcelas','tx_juros','ip','criando_em']
	search_field = ['valor']

admin.site.register(Contrato,ContratoAdmin)

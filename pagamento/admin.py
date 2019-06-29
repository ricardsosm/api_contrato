from django.contrib import admin
from pagamento.models import Pagamento

class PagamentoAdmin(admin.ModelAdmin):

	list_display = ['valor','parcela']
	search_field = ['valor']

admin.site.register(Pagamento,PagamentoAdmin)

from django.contrib import admin
from banco.models import Banco

class BancoAdmin(admin.ModelAdmin):
	
	list_display = ['nome','num_banco','ag']
	search_field = ['nome']

admin.site.register(Banco,BancoAdmin)

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from pagamento.models import Pagamento
from cliente.models import Cliente
from contrato.models import Contrato
from .serializers import PagamentoSerializer

class PagamentoViewSet(viewsets.ModelViewSet):

    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
    	user =  User.objects.get(id=self.request.user.id)
    	print('user ', user)
    	cli = Cliente.objects.filter(user=user or None)
    	if cli:
    		con = Contrato.objects.filter(id_cliente = cli.id)
    		print('cli ', cli.id)
    		if con:
    			self.queryset = Pagamento.objects.filters(id_contrato = con.id)
    		return self.queryset
    	else:
	    	return None

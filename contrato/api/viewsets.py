from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from contrato.models import Contrato
from pagamento.models import Pagamento
from cliente.models import Cliente
from .serializers import ContratoSerializer

class ContratoViewSet(viewsets.ModelViewSet):

    serializer_class = ContratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
    	username = self.request._user
    	user = User.objects.get(username=username)
    	cliente = Cliente.objects.filter(user=user)
    	if cliente:
    		queryset = Contrato.objects.all()
    		return queryset

    @action(methods=['get'], detail=True)
    def divida(self, request,pk=None):
    	resp = {}
    	pagamento = Pagamento.objects.filter(id_contrato=pk)
    	num = 0 
    	if Pagamento:
    		for se in pagamento:
	    		num = se.parcela

    	contrato = Contrato.objects.get(pk=pk)

    	con = contrato.parcelas
    	part = contrato.valor / contrato.parcelas
    	cont = con-num
    	valor = (part * (1.0 + contrato.tx_juros))
    	valor = valor * cont

    	return Response({'valor_devido':valor})
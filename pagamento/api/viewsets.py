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
        username = self.request._user
        user = User.objects.get(username=username)
        cli = Cliente.objects.filter(user=user)
        if cli:
            self.queryset = Pagamento.objects.all()
            return self.queryset


from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from contrato.models import Contrato
from .serializers import ContratoSerializer

class ContratoViewSet(viewsets.ModelViewSet):

    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

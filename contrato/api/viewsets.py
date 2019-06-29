from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from contrato.models import Contrato
from .serializers import ContratoSerializer

class ContratoViewSet(viewsets.ModelViewSet):

    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


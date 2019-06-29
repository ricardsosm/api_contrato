from rest_framework import serializers
from contrato.models import Contrato

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ('id', 'valor', 'parcelas','tx_juros','ip','id_banco','id_cliente')
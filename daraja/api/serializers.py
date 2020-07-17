from rest_framework import serializers
from daraja.models import ExpressPay


class ExpressCallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressPay
        fields = ["id",]

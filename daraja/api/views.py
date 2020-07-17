from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from daraja.api.serializers import ExpressCallbackSerializer
from daraja.models import ExpressPay


class ExpressCallback(CreateAPIView):
    queryset = ExpressPay.objects.all()
    serializer_class = ExpressCallbackSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)

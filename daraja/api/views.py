from datetime import datetime
import pytz

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from daraja.api.serializers import ExpressCallbackSerializer
from daraja.models import ExpressPay
from pypay import loggers


class ExpressCallback(CreateAPIView):
    queryset = ExpressPay.objects.all()
    serializer_class = ExpressCallbackSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        loggers.log_pay('Txn Start')
        loggers.log_pay(request.data)
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code = request.data['Body']['stkCallback']['ResultCode']
        result_desc = request.data['Body']['stkCallback']['ResultDesc']
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        balance = ""
        txn_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        str_txn_date = str(txn_date)
        txn_datetime = datetime.strptime(str_txn_date, "%Y%m%d%H%M%S")
        # aware_txn_datetime = pytz.utc.localize(txn_datetime)
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        txn = ExpressPay.objects.create(
            MerchantRequestID = merchant_request_id,
            CheckoutRequestID = checkout_request_id,
            ResultCode = result_code,
            ResultDesc = result_desc,
            Amount = amount,
            MpesaReceiptNumber = receipt_number,
            Balance = balance,
            TransactionDate = txn_datetime,
            PhoneNumber = phone_number
        )
        txn.save()
        loggers.log_pay('Txn End\n')
        print(request.data)
        return Response(data={'message': 'success'}, status=status.HTTP_201_CREATED)


class C2BValidation(CreateAPIView):
    queryset = ExpressPay.objects.all()
    serializer_class = ExpressCallbackSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        loggers.log_pay('Txn Start')
        loggers.log_pay(request.data)
        loggers.log_pay('Txn End')
        print(request.data)
        return Response(data={'message': 'success'}, status=status.HTTP_201_CREATED)
from datetime import datetime

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
        loggers.log_pay('This worked...')
        loggers.log_pay(request.data)
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        loggers.log_pay({'MerchantRequestID': merchant_request_id})
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        loggers.log_pay({'CheckoutRequestID': checkout_request_id})
        result_code = request.data['Body']['stkCallback']['ResultCode']
        loggers.log_pay({'ResultCode': result_code})
        result_desc = request.data['Body']['stkCallback']['ResultDesc']
        loggers.log_pay({'ResultDesc': result_desc})
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        loggers.log_pay({'Amount': amount})
        receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        loggers.log_pay({'MpesaReceiptNumber': receipt_number})
        balance = ""
        loggers.log_pay({'Balance': balance})
        txn_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        loggers.log_pay({'TransactionDate': txn_date})
        str_txn_date = str(txn_date)
        loggers.log_pay({'TransactionDate': str_txn_date})
        txn_datetime = datetime.strptime(str_txn_date, "%Y%m%d%H%M%S")
        loggers.log_pay({'TransactionDate': txn_datetime})
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']
        loggers.log_pay({'PhoneNumber': phone_number})

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
        print(request.data)
        return Response(data={'message': 'success'}, status=status.HTTP_201_CREATED)

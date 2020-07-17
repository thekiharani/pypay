from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from daraja.api.serializers import ExpressCallbackSerializer
from daraja.models import ExpressPay
from pypay import loggers


class ExpressCallback(CreateAPIView):
    queryset = ExpressPay.objects.all()
    serializer_class = ExpressCallbackSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        loggers.log_pay(request.data)
        print(request.data)

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
        receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['MpesaReceiptNumber']
        loggers.log_pay({'Amount': amount})
        balance = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]['Balance']
        loggers.log_pay({'Balance': balance})
        txn_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['TransactionDate']
        loggers.log_pay({'TransactionDate': txn_date})
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['PhoneNumber']
        loggers.log_pay({'PhoneNumber': phone_number})

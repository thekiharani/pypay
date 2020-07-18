from django.db import models
from django.utils.translation import ugettext_lazy as _

class ExpressPay(models.Model):
    MerchantRequestID = models.CharField(max_length=50)
    CheckoutRequestID = models.CharField(max_length=50)
    ResultCode = models.IntegerField()
    ResultDesc = models.CharField(max_length=100)
    Amount = models.FloatField(max_length=20)
    MpesaReceiptNumber = models.CharField(max_length=20)
    Balance = models.CharField(max_length=20, blank=True, null=True)
    TransactionDate = models.DateTimeField(max_length=20)
    PhoneNumber = models.CharField(max_length=20)

    class Meta:
        db_table = "payments_lipanampesa"
        verbose_name = _("Lipa na MPESA")
        verbose_name_plural = _("Lipa na MPESA")
        ordering = ['-TransactionDate']

    def __str__(self):
        return self.MpesaReceiptNumber

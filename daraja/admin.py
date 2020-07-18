from django.contrib import admin

from daraja.models import ExpressPay

class ExpressPayAdmin(admin.ModelAdmin):
    list_display = ('PhoneNumber', 'Amount', 'MpesaReceiptNumber', 'TransactionDate')

admin.site.register(ExpressPay, ExpressPayAdmin)

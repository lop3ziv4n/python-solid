from models.invoice import Invoice


class NotificationService:

    def emailInvoice(self, invoice: Invoice):
        # code email invoice
        print('send email invoice')

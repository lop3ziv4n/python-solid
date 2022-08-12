from models.invoice import Invoice
from models.order import Order


class InvoiceService:

    def createInvoice(self, order: Order):
        # code create invoice
        print('create invoice')
        return Invoice

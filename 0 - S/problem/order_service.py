from models.invoice import Invoice
from models.order import Order


class OrderService:

    def saveOrder(self, order: Order):
        try:
            self._insertOrder(order)
            invoice = self._createInvoice(order)
            self._emailInvoice(invoice)
            f = open("infoLog.txt", "a")
            f.write("the order has be complete")
            f.close()
        except Exception as e:
            f = open("errorLog.txt", "a")
            f.write(type(e).__name__)
            f.close()

    def _insertOrder(self, order):
        # code insert order in database
        print('insert order')

    def _createInvoice(self, order):
        # code create invoice
        print('create invoice')
        return Invoice

    def _emailInvoice(self, invoice):
        # code send email invoice
        print('send email invoice')

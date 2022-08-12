from invoice_service import InvoiceService
from logger_service import LoggerService
from models.order import Order
from notification_service import NotificationService
from order_repository import OrderRepository


class OrderService:

    def __init__(self):
        self._orderRepository = OrderRepository()
        self._invoiceService = InvoiceService()
        self._notificationService = NotificationService()
        self._loggerService = LoggerService()

    def saveOrder(self, order: Order):
        try:
            self._orderRepository.insertOrder(order)
            invoice = self._invoiceService.createInvoice(order)
            self._notificationService.emailInvoice(invoice)
            self._loggerService.debug("the order has be complete")
        except Exception as e:
            self._loggerService.error(type(e).__name__)

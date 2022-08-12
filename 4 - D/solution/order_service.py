from event_notification_service import EventNotificationService
from models.order import Order


class OrderService:

    def __init__(self, eventNotificationService: EventNotificationService):
        self._eventNotificationService = eventNotificationService

    def generateOrder(self, order: Order):
        # code order create

        # send notification event
        self._eventNotificationService.logEvent("The order was successfully created")

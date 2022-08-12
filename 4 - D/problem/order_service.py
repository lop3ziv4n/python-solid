from models.order import Order


class DataLogService:

    def logEvent(self, message: str):
        # code event on DataLog
        print(message)


class OrderService:

    def __init__(self):
        self._dataLogService = DataLogService()

    def generateOrder(self, order: Order):
        # code order create

        # send notification DataLog
        self._dataLogService.logEvent("The order was successfully created")

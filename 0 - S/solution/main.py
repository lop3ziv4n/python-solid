from models.order import Order
from order_service import OrderService

if __name__ == '__main__':
    order = Order()
    service = OrderService()
    service.saveOrder(order)

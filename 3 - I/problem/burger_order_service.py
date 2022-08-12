from food_order_service import IFoodOrderService


class BurgerOrderService(IFoodOrderService):

    def orderBurger(self, quantity: int):
        # code order burger
        print("code Burger")

    def orderSteak(self, quantity: int):
        raise NotImplementedError()

    def orderSalad(self, quantity: int):
        raise NotImplementedError()

from abc import ABC, abstractmethod


class IFoodOrderService(ABC):

    @abstractmethod
    def orderBurger(self, quantity: int):
        pass

    @abstractmethod
    def orderSteak(self, quantity: int):
        pass

    @abstractmethod
    def orderSalad(self, quantity: int):
        pass

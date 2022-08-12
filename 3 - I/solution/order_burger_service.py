from abc import ABC, abstractmethod


class IOrderBurgerService(ABC):

    @abstractmethod
    def orderBurger(self, quantity: int):
        pass

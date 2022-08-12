from abc import ABC, abstractmethod


class IOrderSaladService(ABC):

    @abstractmethod
    def orderSalad(self, quantity: int):
        pass

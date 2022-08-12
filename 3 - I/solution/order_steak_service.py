from abc import ABC, abstractmethod


class IOrderSteakService(ABC):

    @abstractmethod
    def orderSteak(self, quantity: int):
        pass

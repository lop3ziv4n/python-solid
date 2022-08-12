from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def speedUp(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def park(self):
        pass

    @abstractmethod
    def takeOff(self):
        pass

    @abstractmethod
    def land(self):
        pass

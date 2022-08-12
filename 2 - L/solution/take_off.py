from abc import ABC, abstractmethod


class TakeOff(ABC):

    @abstractmethod
    def takeOff(self):
        pass

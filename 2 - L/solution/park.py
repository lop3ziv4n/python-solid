from abc import ABC, abstractmethod


class Park(ABC):

    @abstractmethod
    def park(self):
        pass

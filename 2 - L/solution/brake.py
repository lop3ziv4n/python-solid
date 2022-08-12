from abc import ABC, abstractmethod


class Brake(ABC):

    @abstractmethod
    def brake(self):
        pass

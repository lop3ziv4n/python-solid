from abc import ABC, abstractmethod

from models.order import Order


class ReportGenerator(ABC):

    @abstractmethod
    def createReport(self, order: Order):
        pass

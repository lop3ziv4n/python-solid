from abc import ABC, abstractmethod


class EventNotificationService(ABC):

    @abstractmethod
    def logEvent(self, message: str):
        pass

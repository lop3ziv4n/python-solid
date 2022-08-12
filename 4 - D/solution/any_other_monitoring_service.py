from event_notification_service import EventNotificationService


class AnyOtherMonitoringService(EventNotificationService):

    def logEvent(self, message: str):
        # code event on other monitoring
        print(message)

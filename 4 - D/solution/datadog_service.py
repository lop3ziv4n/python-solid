from event_notification_service import EventNotificationService


class DataLogService(EventNotificationService):

    def logEvent(self, message: str):
        # code event on DataLog
        print(message)

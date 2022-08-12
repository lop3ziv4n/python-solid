from models.order import Order
from models.report_type import ReportType
from report_service import ReportService

if __name__ == '__main__':
    order = Order()  # Get order from database
    service = ReportService()
    service.generateReport(order, ReportType.PDF)

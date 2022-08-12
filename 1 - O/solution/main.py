from models.order import Order
from report_generator_pdf import ReportGeneratorPDF
from report_service import ReportService

if __name__ == '__main__':
    order = Order()  # Get order from database
    service = ReportService(ReportGeneratorPDF())  # Send implementation
    service.generateReport(order)

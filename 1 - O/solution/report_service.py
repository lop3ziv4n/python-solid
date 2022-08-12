from models.order import Order
from report_generator import ReportGenerator


class ReportService:

    def __init__(self, reportGenerator: ReportGenerator):
        self._reportGenerator = reportGenerator

    def generateReport(self, order: Order):
        # code create report
        self._reportGenerator.createReport(order)

from models.order import Order
from models.report_type import ReportType


class ReportService:

    def generateReport(self, order: Order, type: ReportType):
        # code create report
        # specific conversion depending on type
        if type == ReportType.PDF:
            self._createPDFReport(order)
        elif type == ReportType.EXCEL:
            self._createExcelReport(order)

    def _createPDFReport(self, order: Order):
        # create pdf report
        print('create pdf report')

    def _createExcelReport(self, order: Order):
        # create excel report
        print('create excel report')

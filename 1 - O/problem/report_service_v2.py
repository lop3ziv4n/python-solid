from models.order import Order
from models.report_type_v2 import ReportTypeV2


class ReportServiceV2:

    def generateReport(self, order: Order, type: ReportTypeV2):
        # code create report
        # specific conversion depending on type
        if type == ReportTypeV2.PDF:
            self._createPDFReport(order)
        elif type == ReportTypeV2.EXCEL:
            self._createExcelReport(order)
        elif type == ReportTypeV2.JSON:
            self._createJSONReport(order)
        elif type == ReportTypeV2.XML:
            self._createXMLReport(order)

    def _createPDFReport(self, order: Order):
        # create pdf report
        print('create pdf report')

    def _createExcelReport(self, order: Order):
        # create excel report
        print('create excel report')

    def _createJSONReport(self, order: Order):
        # create json report
        print('create json report')

    def _createXMLReport(self, order: Order):
        # create xml report
        print('create xml report')

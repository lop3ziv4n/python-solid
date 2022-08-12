from models.order import Order
from report_generator import ReportGenerator


class ReportGeneratorPDF(ReportGenerator):

    def createReport(self, order: Order):
        # create pdf report
        print('create pdf report')

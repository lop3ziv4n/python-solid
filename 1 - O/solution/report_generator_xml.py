from models.order import Order
from report_generator import ReportGenerator


class ReportGeneratorXML(ReportGenerator):

    def createReport(self, order: Order):
        # create xml report
        print('create xml report')

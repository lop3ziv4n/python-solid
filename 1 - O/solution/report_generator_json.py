from models.order import Order
from report_generator import ReportGenerator


class ReportGeneratorJson(ReportGenerator):

    def createReport(self, order: Order):
        # create json report
        print('create json report')

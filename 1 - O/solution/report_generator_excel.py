from models.order import Order
from report_generator import ReportGenerator


class ReportGeneratorExcel(ReportGenerator):

    def createReport(self, order: Order):
        # create excel report
        print('create excel report')

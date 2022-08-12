from brake import Brake
from park import Park
from speed_up import SpeedUp


class Bike(Brake, Park, SpeedUp):

    def brake(self):
        # code Brake
        print("code Brake")

    def park(self):
        # code Park
        print("code Park")

    def speedUp(self):
        # code SpeedUp
        print("code SpeedUp")

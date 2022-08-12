from land import Land
from take_off import TakeOff


class Car(TakeOff, Land):

    def takeOff(self):
        # code TakeOff
        print("code TakeOff")

    def land(self):
        # code Land
        print("code Land")

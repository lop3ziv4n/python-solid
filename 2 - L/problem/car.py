from vehicle import Vehicle


class Car(Vehicle):

    def brake(self):
        # code Brake
        print("code Brake")

    def park(self):
        # code Park
        print("code Park")

    def takeOff(self):
        raise NotImplementedError()

    def land(self):
        raise NotImplementedError()

    def speedUp(self):
        # code SpeedUp
        print("code SpeedUp")

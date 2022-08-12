from vehicle import Vehicle


class Plane(Vehicle):

    def brake(self):
        raise NotImplementedError()

    def park(self):
        raise NotImplementedError()

    def takeOff(self):
        # code TakeOff
        print("code TakeOff")

    def land(self):
        # code Land
        print("code Land")

    def speedUp(self):
        raise NotImplementedError()

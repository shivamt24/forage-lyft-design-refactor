from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        sum = 0
        for i in self.tire_array:
            sum += i

        return sum >= 3.0

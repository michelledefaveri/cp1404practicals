from prac_09.car import Car

class UnreliableCar(Car):
    """A version of a Car that is unreliable."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar object."""
        super().__init__(name, fuel)
        self.reliability = reliability








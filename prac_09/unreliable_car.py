"""
CP1404 Practical 9
Unreliable Car
"""

import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A version of a Car that is unreliable."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar object."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car."""
        random_float = random.uniform(0,100)
        if random_float < self.reliability:
            return super().drive(distance)
        return 0
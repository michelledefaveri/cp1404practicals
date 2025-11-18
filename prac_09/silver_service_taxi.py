"""
Practical 9
SilverServiceTaxi
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised taxi that includes fanciness multiplier and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare distance."""
        return super().get_fare()+self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"






from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Initialise a SilverServiceTaxi."""
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness





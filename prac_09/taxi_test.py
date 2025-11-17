""""Taxi test"""

from taxi import Taxi

def main():
    """Test taxi class."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    print(my_taxi)

main()
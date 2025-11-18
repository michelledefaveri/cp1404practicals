from silver_service_taxi import SilverServiceTaxi

def main():
    """Run tests for SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)

    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(f"Fare for an 18km trip with fanciness 2 is ${fare:.2f}")

    assert abs(fare-48.78) < 0.01, f"Expected 48.78 and got {fare:.2f}"

main()
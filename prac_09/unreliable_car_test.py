from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar behaviour."""
    reliable_car = UnreliableCar("Almost New", 100, 90)
    unreliable_car = UnreliableCar("Very Old", 100, 10)

    print("Testing reliability of cars.")
    for i in range(10):
        print(f"Attempt {i+1}")
        print(f"{reliable_car.name} drove {reliable_car.drive(20)} km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(20)} km")

main()
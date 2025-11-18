from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Run the taxi simulator program."""
    total_bill = 0
    current_taxi = None

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far?"))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print (f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    """Ask user to choose a taxi and return it."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def display_taxis(taxis):
    """Print the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

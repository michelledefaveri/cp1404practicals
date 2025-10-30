"""
Estimated time = 25 minutes
Actual time = 29 minutes
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2025

def run_tests():
    """Run test on Guitar class methods."""
    # Create test guitars
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1000.00)

    # Test get_age()
    print(f"{guitar.name} get_age() - Expected {CURRENT_YEAR - 1922}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {CURRENT_YEAR - 2013}. Got {other.get_age()}")

    # Test is_vintage()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")

if __name__ == "__main__":
    run_tests()


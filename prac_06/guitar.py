"""
Estimated time = 35 minutes
Actual time = 37 minutes
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Guitar class for storing attributes of a guitar."""

    def __init__(self, name="", year=0, cost=""):
        """Initialise a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print guitar details."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage (over 50 years old)."""
        return self.get_age() >= VINTAGE_AGE





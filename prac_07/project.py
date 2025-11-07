from datetime import date

class Project:
    """Represent a project."""

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion: int):
        """Initialize project attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def is_complete(self):
        """Return True if the project is 100% complete, otherwise False."""
        return self.completion >= 100

    def update_completion(self, completion_value):
        """Update completion to the given value."""
        self.completion = completion_value

    def update_priority(self, priority_value):
        """Update priority to the given value."""
        self.priority = priority_value

    def get_start_date(self):
        """Return the start date."""
        return self.start_date

    def __lt__(self, other):
        """Default sorting by priority."""
        return self.priority < other.priority

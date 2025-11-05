from datetime import date

class Project:
    """Represents a single project."""

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion: int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def is_complete(self):
        return self.completion >= 100


    def get_start_date(self):
        return self.start_date


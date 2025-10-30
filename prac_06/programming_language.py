"""
Estimated time = 20 minutes
Actual time = 31 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language with its properties."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a formatted string describing the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the program is dynamically typed or False if it is not."""
        return self.typing.lower() == "dynamic"




"""
Practical 9
Band Class
"""

class Band:
    """Band class containing list of musicians."""
    def __init__(self, name = ""):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band with its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a Musician object to the band."""
        self.musicians.append(musician)


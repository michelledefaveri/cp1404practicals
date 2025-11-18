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


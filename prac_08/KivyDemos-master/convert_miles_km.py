"""
CP1404 - Practical 08
GUI Program to Convert Miles to Kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesToKilometerConverterApp(App):
    """App to convert miles to kilometres."""
    output_text = StringProperty('0.0')

    def build(self):
        """Load KV layout."""
        self.title = "Convert Miles to Kilometres."
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Calculate kilometres from miles."""
        miles = self.get_miles_value()
        result = miles * MILES_TO_KM
        self.output_text = str(result)

    def get_miles_value(self):
        """Return miles input as float or 0 if invalid."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        return miles

    def handle_increment(self, change):
        """Increase miles by change (+1 or -1)."""
        miles = self.get_miles_value() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

MilesToKilometerConverterApp().run()

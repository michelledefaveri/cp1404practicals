from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesToKilometerConverterApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres."
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        miles = self.get_miles_value()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_miles_value(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        return miles



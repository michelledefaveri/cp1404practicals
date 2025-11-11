from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesToKilometerConverterApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres."
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


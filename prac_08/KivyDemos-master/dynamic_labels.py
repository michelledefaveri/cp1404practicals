"""
CP1404 - Practical 08
GUI Program for Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """App for Dynamic Labels."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # List of names
        self.names = ["Kai", "Bob", "Jack", "Sandra", "Mia"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name."""
        for name in self.names:
            dynamic_label = Label(text=name)
            self.root.ids.main.add_widget(dynamic_label)

DynamicLabelsApp().run()

# Sample spinner app in kivy
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from kivy.uix.floatlayout import FloatLayout

from kivy.app import App


# Make an App by deriving from the App class
class SpinnerExample(App):
    def build(self):
        layout = FloatLayout()

        # configure spinner object and add to layout
        self.spinnerObject = Spinner(text="Python", values=("Python", "Java", "C++"))
        self.spinnerObject.size_hint = (0.3, 0.2)
        self.spinnerObject.pos_hint = {'x': .1, 'y': .75}
        layout.add_widget(self.spinnerObject)
        self.spinnerObject.bind(text=self.on_spinner_select)

        # add a label displaying the selection from the spinner
        self.spinnerSelection = Label(text="Selected value in spinner is: %s" % self.spinnerObject.text)
        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint = {'x': .1, 'y': .3}

        return layout

    # call back for the selection in spinner object
    def on_spinner_select(self, spinner, text):
        self.spinnerSelection.text = "Selected value in spinner is: %s" % self.spinnerObject.text
        # print('The spinner', spinner, 'have text', text)


# Run the app
if __name__ == '__main__':
    SpinnerExample().run()

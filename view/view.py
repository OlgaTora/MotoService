"""
    Use this file, as well as other files you may create in this folder,
    for code directly related to the app view.
"""

from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from controller import controller
from kivy.config import Config
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

Window.size = (450, 750)
Config.set('kivy', 'keyboard_mode', 'system')
Config.write()
Builder.load_file('./view/ms.kv')


class AppScreenManager(ScreenManager):
    motorcycles = ObjectProperty(None, allownone=True)
    clients = ObjectProperty(None, allownone=True)
    motorcycle_form = ObjectProperty(None, allownone=True)
    client_form = ObjectProperty(None, allownone=True)

    def __init__(self, *args):
        super(AppScreenManager, self).__init__(*args)
        # self.ids.scroll.size = (200, Window.height)
        # self.ids.list.bind(minimum_height=self.ids.list.setter('height'))
        # self.set_motorcycles()
        # self.set_item_list()

    """
        Get the items from the database and display them on the ScrollView
    """
    # def set_item_list(self):
    #
    #     items = controller.get_items()
    #
    #     for item in items:
    #         self.ids.list.add_widget(Button(text=item.name, id=str(item.id), color=(0, 0, 0, 1),
    #                     background_color=(.9, 9, 9, 0), font_size=30,
    #                     halign='left', size_hint_y=None, height=30))

    """
        Set the values for the Category spinner
    """
    def choice_motocycle_model(self, *args):
        return controller.get_base_motorcycles()

    def set_motorcycles(self):
        self.motorcycles = controller.get_motorcycles()
        for moto in self.motorcycles:
            pass
            # self.ids.motorcycles.values.append(moto.name)

    def set_clients(self):
        self.clients = controller.get_clients()
        for client in self.clients:
            pass
            # self.ids.motorcycles.values.append(moto.name)

    def add_motorcycle(*args):
        print(args)
        root = args[0]
        if not root.motorcycle_form.name.text:
            return

        controller.add_motorcycle({
            'name': root.motorcycle_form.name.text,
            'document': root.motorcycle_form.document.text,
        })

        root.ids.motorcycles.values = []
        root.set_motorcycles()
        # root.cancel_motorcycle()

    def add_client(*args):
        root = args[0]
        if not root.client_form.name.text:
            return

        controller.add_client({
            'name': root.client_form.name.text,
        })

        root.ids.clients.values = []
        root.set_clients()
        # root.cancel_motorcycle()

    def cancel_motorcycle(self, *args):
        self.ids.input_area.remove_widget(self.motorcycle_form)
        self.motorcycle_form = None

    def open_motorcycle_form(self, *args):
        self.motorcycle_form = MotorcycleAddForm(self)
        self.ids.input_area.add_widget(self.motorcycle_form)

    def open_client_form(self, *args):
        self.client_form = ClientAddForm(self)
        self.ids.input_area.add_widget(self.client_form)

    # def add_item(self):
    #     if not self.ids.item.text:
    #         return
    #     cat = [c for c in self.categories if c.name == self.ids.categories.text][0]
    #     controller.add_item({"name": self.ids.item.text, "cat_id": cat.id})
    #     self.ids.item.text = ''
    #     self.ids.list.clear_widgets()
    #     self.set_item_list()


class MotorcycleAddForm(GridLayout):
    def __init__(self, root, *args, **kwargs):
        super(MotorcycleAddForm, self).__init__(*args, **kwargs)
        self.name = TextInput(hint_text='Модель')
        self.add_widget(self.name)
        self.document = TextInput(hint_text='Номерной знак')
        self.add_widget(self.document)
        self.add_widget(Button(text='Добавить', on_press=root.add_motorcycle))
        # self.add_widget(
        #     Button(text='Удалить', on_press=root.cancel_motorcycle))
        self.cols = 1
        self.spacing = 5
        self.size_hint = (0.9, 0.3)
        self.pos_hint = {'x': .05, 'y': .5}


class ClientAddForm(GridLayout):
    def __init__(self, root, *args, **kwargs):
        super(ClientAddForm, self).__init__(*args, **kwargs)
        self.name = TextInput(hint_text='Имя')
        self.add_widget(self.name)
        # self.moto = TextInput.selection_text('f')
        self.add_widget(DropDown())#text='CHOICE', on_press=root.choice_motocycle_model))
        self.add_widget(Button(text='Добавить', on_press=root.add_client))
        # self.add_widget(
        #     Button(text='Удалить', on_press=root.cancel_motorcycle))
        self.cols = 1
        self.spacing = 5
        self.size_hint = (0.9, 0.3)
        self.pos_hint = {'x': .05, 'y': .5}


class MotoApp(App):
    def build(self):
        return AppScreenManager()

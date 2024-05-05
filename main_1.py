# from kivy.lang import Builder
# from kivymd.app import MDApp
# import sqlite3
from functools import partial

from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from controller import controller


class RootWidget(FloatLayout):
    client_form = ObjectProperty(None, allownone=True)
    clients = ObjectProperty(None, allownone=True)
    motorcycle_form = ObjectProperty(None, allownone=True)
    motorcycles = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='Add Client',
                               size_hint=(0.25, 0.15),
                               pos_hint={'center_x': .5, 'center_y': .5},
                               on_press=self.open_client_form))
        self.add_widget(Button(text="Bye", size_hint=(0.25, 0.15),
                               pos_hint={'center_x': .5, 'center_y': .3}))

    def open_client_form(self, *args):
        self.client_form = ClientAddForm(self)
        self.add_widget(self.client_form)

    def open_motorcycle_form(self, *args):
        self.motorcycle_form = MotorcycleAddForm(self)
        self.add_widget(self.motorcycle_form)

    def set_clients(self):
        self.clients = controller.get_clients()

    def set_motorcycles(self):
        self.motorcycles = controller.get_motorcycles()

    def add_client(*args):
        root = args[0]
        if not root.client_form.name.text:
            return

        controller.add_client({
            'name': root.client_form.name.text,
            # 'motorcycle': root.client_form.motorcycle.text,
        })

        # root.clients.values = []
        root.set_clients()
        # root.cancel_motorcycle()

    def add_moto(*args):
        root = args[0]
        if not root.motorcycle_form.name.text:
            return

        controller.add_motorcycle({
            'name': root.motorcycle_form.name.text,
            'document': root.motorcycle_form.document.text,
        })

        # root.clients.values = []
        root.set_motorcycles()
        # root.cancel_motorcycle()

    def add_new(*args):
        root = args[0]
        if not root.motorcycle_form.name.text:
            return
        controller.add_motorcycle({
            'name': root.motorcycle_form.name.text,
            'document': root.motorcycle_form.document.text,
        })

        controller.add_client({
            'name': root.motorcycle_form.client_name.text,
            'motorcycle_id': controller.get_motorcycle(root.motorcycle_form.name.text),
        })


        # root.clients.values = []
        root.set_motorcycles()
        # root.cancel_motorcycle()
class MotoServiceApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 1, 1, .5)
            self.rect = Rectangle(
                size=root.size,
                pos=root.pos,
                source='Harley Davidson.jpeg', )
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class ClientAddForm(GridLayout):
    def __init__(self, root, *args, **kwargs):
        super(ClientAddForm, self).__init__(*args, **kwargs)
        # self.name = TextInput(hint_text='Имя')
        # self.add_widget(self.name)
        self.add_widget(Button(text='Add Moto if no in DB',
                               size_hint=(0.25, 0.15),
                               pos_hint={'center_x': .5, 'center_y': .5},
                               on_press=root.open_motorcycle_form))
        self.add_widget(Button(text='Add Moto if in DB'))#, on_press=root.add_client))
        # spinnerObject.bind(text=self.on_spinner_select)
        # self.add_widget(Button(text='Добавить', on_press=root.add_client))
        # self.add_widget(
        #     Button(text='Удалить', on_press=root.cancel_motorcycle))
        self.cols = 1
        self.spacing = 5
        self.size_hint = (0.9, 0.3)
        self.pos_hint = {'x': .05, 'y': .5}


class MotorcycleAddForm(GridLayout):
    def __init__(self, root, *args, **kwargs):
        super(MotorcycleAddForm, self).__init__(*args, **kwargs)
        self.client_name = TextInput(hint_text='Имя')
        self.add_widget(self.client_name)
        self.document = TextInput(hint_text='document')
        self.add_widget(self.document)
        motos = [str(moto) for moto in controller.get_base_motorcycles()]
        self.name = Spinner(text="Moto", values=motos)
        self.add_widget(Button(text='Add client and new moto', on_press=root.add_new))
        # self.add_widget(Button(text='Добавить', on_press=root.add_moto))
        self.name.size_hint = (0.4, 0.7)
        self.name.pos_hint = {'x': .1, 'y': .75}
        self.add_widget(self.name)
        self.cols = 1
        self.spacing = 5
        self.size_hint = (0.9, 0.3)
        self.pos_hint = {'x': .05, 'y': .5}

# class MotoyApp(App):
#     def build(self):
#         lable = Label(text='Мото Сервис Виталия',halign='center',
#                     font_size=30, size_hint=(1, .2), pos_hint= {'x': 0, 'top': .9})
#         floatlayout = FloatLayout(pos_hint= {'x': 0, 'top': 1}, size_hint= (1, .1))
#         button1 = Button(text="Hi", size_hint=(0.25, 0.18), pos=(350, 100))
#         button2 = Button(text="Bye", size_hint=(0.25, 0.18), pos=(350, 200))
#         # button2.bind(on_press=partial(self.com2, button2))
#         boxlayout = BoxLayout()
#         boxlayout.add_widget(button1)
#         boxlayout.add_widget(lable)
#         return boxlayout


if __name__ == '__main__':
    MotoServiceApp().run()
#
# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "BlueGray"
#
#         conn = sqlite3.connect('ms.db')
#
#         cursor = conn.cursor()
#
#         # Create A Table
#         cursor.execute("""CREATE TABLE if not exists customers (name text) """)
#
#         # Commit our changes
#         conn.commit()
#
#         # Close our connection
#         conn.close()
#
#         return Builder.load_file('view/ms.kv')
#
#     def submit(self):
#         # Create Database Or Connect To One
#         conn = sqlite3.connect('ms.db')
#
#         # Create A Cursor
#         c = conn.cursor()
#
#         # Add A Record
#         c.execute("INSERT INTO customers VALUES (:first)",
#                   {
#                       'first': self.root.ids.word_input.text,
#                   })
#
#         # Add a little message
#         self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'
#
#         # Clear the input box
#
#         self.root.ids.word_input.text = ''
#
#         # Commit our changes
#         conn.commit()
#
#         # Close our connection
#         conn.close()
#
#     def show_records(self):
#         # Create Database Or Connect To One
#         conn = sqlite3.connect('ms.db')
#
#         # Create A Cursor
#         c = conn.cursor()
#
#         # Grab records from database
#         c.execute("SELECT * FROM customers")
#         records = c.fetchall()
#
#         word = ''
#         # Loop thru records
#         for record in records:
#             word = f'{word}\n{record[0]}'
#             self.root.ids.word_label.text = f'{word}'
#
#         # Commit our changes
#         conn.commit()
#
#         # Close our connection
#         conn.close()
#
#
# if __name__ == '__main__':
#     MainApp().run()

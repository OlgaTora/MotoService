import requests
import delphifmx

BASE = 'http://127.0.0.1:8000/'


class ClientManager(delphifmx.Form):

    def __init__(self, owner):
        self.SetProps(Caption='Clients Management', OnShow=self.__form_show)

        self.document = delphifmx.Label(self)
        self.document.SetProps(Parent=self, Text='Document: ', Position=delphifmx.Position(delphifmx.PointF(20, 20)))

        self.surname = delphifmx.Label(self)
        self.surname.SetProps(Parent=self, Text='Surname: ', Position=delphifmx.Position(delphifmx.PointF(20, 45)))

        self.firstname = delphifmx.Label(self)
        self.firstname.SetProps(Parent=self, Text='First Name: ', Position=delphifmx.Position(delphifmx.PointF(20, 70)))

        self.patronymic = delphifmx.Label(self)
        self.patronymic.SetProps(Parent=self, Text='Patronymic: ',
                                 Position=delphifmx.Position(delphifmx.PointF(20, 95)))

        self.birthday = delphifmx.Label(self)
        self.birthday.SetProps(Parent=self, Text='Birthday: ', Position=delphifmx.Position(delphifmx.PointF(20, 120)))

        self.id = delphifmx.Label(self)
        self.id.SetProps(Parent=self, Text='ID: ', Position=delphifmx.Position(delphifmx.PointF(460, 120)))
        
        # Creating a TextBoxs.
        self.editDocument = delphifmx.Edit(self)
        self.editDocument.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(100, 20)), Height=25)

        self.editSurname = delphifmx.Edit(self)
        self.editSurname.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(100, 45)), Height=25)

        self.editFirstName = delphifmx.Edit(self)
        self.editFirstName.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(100, 70)), Height=25)

        self.editPatronymic = delphifmx.Edit(self)
        self.editPatronymic.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(100, 95)), Height=25)

        self.editBirthday = delphifmx.Edit(self)
        self.editBirthday.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(100, 120)), Height=25)

        self.editId = delphifmx.Edit(self)
        self.editId.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(480, 120)), Height=25)
        
        self.addClient = delphifmx.Button(self)
        self.addClient.SetProps(Parent=self, Text='Add new Client',
                                Position=delphifmx.Position(delphifmx.PointF(220, 150)), Width=130,
                                OnClick=self.__button_click_add)

        self.view = delphifmx.Button(self)
        self.view.SetProps(Parent=self, Text='View Clients', Position=delphifmx.Position(delphifmx.PointF(340, 150)),
                           Width=130,
                           OnClick=self.__button_click_view)

        self.view = delphifmx.Button(self)
        self.view.SetProps(Parent=self, Text='Delete Client', Position=delphifmx.Position(delphifmx.PointF(460, 150)),
                           Width=130,
                           OnClick=self.__button_click_del)

        self.list = delphifmx.ListBox(self)
        self.list.SetProps(Parent=self, Position=delphifmx.Position(delphifmx.PointF(20, 180)), Width=800, Height=250)

    def __form_show(self, sender):
        self.SetProps(Width=900, Height=500)

    def __button_click_add(self, sender):
        new_object = {'document': self.editDocument.text, 'surname': self.editSurname.text,
                      'firstname': self.editFirstName.text,
                      'patronymic': self.editPatronymic.text, 'birthday': self.editBirthday.text}

        x = requests.post(BASE + "create-new-client", json=new_object)
        self.list.items.add(x.text)
        self.list.items.add('New Client was successfully added!')
        self.editDocument.text = self.editSurname.text = self.editFirstName.text = self.editPatronymic.text \
            = self.editBirthday.text = ""

    def __button_click_view(self, sender):
        # Getting all clients from the database.
        response = requests.get(BASE + "get-all-clients")
        response = response.json()
        self.list.items.text = ''
        for client in response:
            self.list.items.add(client)

    def __button_click_del(self, sender):
        # Delete client from the database.
        id2del = int(self.editId.text)
        response = requests.delete(f'{BASE}delete-client/{id2del}')
        self.list.items.add('Client was successfully deleted!')
        self.editId.text = ''



import delphifmx

from Arcitecture.Seminar_10.clinic_gui.clients_manager import ClientManager


def run():
    delphifmx.Application.Initialize()
    delphifmx.Application.Title = "Clinica"
    delphifmx.Application.MainForm = ClientManager(delphifmx.Application)
    delphifmx.Application.MainForm.Show()
    delphifmx.Application.Run()
    delphifmx.Application.MainForm.Destroy()


if __name__ == '__main__':
    run()

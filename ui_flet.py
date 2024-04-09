import tkinter as tk
from database import *

conn, cursor = initialize_connection()


def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')


class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Welcome")
        center_window(240, 120)

        login_button = tk.Button(self, text="Login", width=10, command=self.open_login_window)
        login_button.pack(padx=20, pady=(20, 10))

        register_button = tk.Button(self, text="Register", width=10, command=self.open_register_window)
        register_button.pack(pady=10)
        self.pack()

    def open_login_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()

    # LoginWindow(self.master)

    def open_register_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
    #  RegisterWindow(self.master)


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
WelcomeWindow(root)
root.mainloop()



import tkinter as tk
from assets.style import BG
from screens.screen1_load import Screen1
from screens.screen2_settings import Screen2
from screens.screen3_results import Screen3

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("منسق أرقام الجوال")
        self.geometry("750x650")
        self.resizable(True, True)
        self.configure(bg=BG)

        # Data
        self.df = None
        self.settings = {}
        self.last_settings = {}
        self.valid_rows = []
        self.invalid_rows = []
        self.groups = []

        self.screens = [
            Screen1(self, self),
            Screen2(self, self),
            Screen3(self, self),
        ]
        self.current = 0
        self.show_screen(0)

    def show_screen(self, index):
        self.screens[self.current].pack_forget()
        self.current = index
        screen = self.screens[index]
        if hasattr(screen, "refresh"):
            screen.refresh()
        screen.pack(fill="both", expand=True)

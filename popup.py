import tkinter as tk
from tkinter import messagebox
import os


class POPUP:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Information")
        self.user = os.getlogin()
        self.message()


    def message(self):
        tk.Label(self.root, text=f"The file is in /home/{self.user}/youtube_gui",
                 font=("Source Code Pro Black", 12)).grid(column=0, row=0, padx=10, pady=10)

        tk.Button(self.root, text="Ok", cursor="hand2",
                  font=("Source Code Pro Black", 10), command=self.root.destroy, width=15).grid(column=0, row=1, pady=10)


        self.root.mainloop()

if __name__ == '__main__':
    app = POPUP()
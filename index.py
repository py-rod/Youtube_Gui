import tkinter as tk
from tkinter import messagebox
from data_video import download


class window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Url")
        self.frm = tk.Frame(self.root, padx=10, pady=10)
        self.frm.grid()
        self.url = tk.StringVar()
        self.menu()

    def check(self):
        url = self.url.get()
        print(url[0:23])

        if url[0:23] != "https://www.youtube.com":
            messagebox.showerror(message="Error")
        else:
            download(url)
            self.url.set("")
            

    def menu(self):
        #URL
        tk.Label(self.frm, text="Youtube url: ", font=("Source Code Pro Black", 11)).grid(column=0, row=0)
        tk.Entry(self.frm, textvariable=self.url, font=("Source Code Pro Black", 10),
                 width=50).grid(column=1, row=0)

        tk.Button(self.frm, text="Submit", font=("Source Code Pro Black", 9), cursor="hand2",
                  command=self.check).grid(column=2, row=0, padx=7)



        self.root.mainloop()

if __name__ == '__main__':
    app = window()

from Tkinter import *

class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill = BOTH, expand = 1)

root = Tk()
app = App(root)
root.mainloop()

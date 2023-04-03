from tkinter import ttk

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        self._root.configure(background="grey")
        self._root.minsize(500, 500) 
        

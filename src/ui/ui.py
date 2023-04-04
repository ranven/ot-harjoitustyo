from tkinter import ttk
from ui.project_view import ProjectView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._root.configure(background="grey")
        self._root.minsize(500, 500) 
        self._show_project_view()
        
    def _destroy_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def _show_project_view(self):
        self._destroy_view()
        self._current_view = ProjectView(self._root)
        self._current_view.pack()
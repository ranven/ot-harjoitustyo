from tkinter import ttk, constants
from services.project_service import project_service

class ProjectListView:
    def __init__(self, root, projects):
        self._root = root
        self._projects = projects
        self._frame = None
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()
            
    def _initialize_project(self, project):
        project_frame = ttk.Frame(master=self._frame)
                
        project_created_at = ttk.Label(master=project_frame, text=project.created_at)
        project_created_at.config(font=("Arial", 8))
        project_created_at.grid(row=0, column=0)
        
        project_title = ttk.Label(master=project_frame, text=project.title) 
        project_title.grid(row=1, column=0)
        
        project_frame.config(padding=16, border=2)
        project_frame.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title = ttk.Label(master=self._frame, text="Projects")
        title.config(font=("Arial", 16), padding=8)
        title.pack(fill=constants.X)

        for project in self._projects:
            self._initialize_project(project)
        

class ProjectView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._project_list_view = None
        self._project_list_frame = None
        self._create_project = None
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()
        
    def _initialize_project_list(self):
        if self._project_list_view:
            self._project_list_view.destroy()
            
        projects = project_service.get_all_projects()
        self._project_list_view = ProjectListView(self._project_list_frame, projects)
        self._project_list_view.pack()
        
    def _handle_add_project(self):
        project_title = self._create_project.get()
        if project_title:
            project_service.create_project(project_title)
            self._initialize_project_list()
            self._create_project.delete(0, constants.END)
        
    def _initialize_footer(self):
        self._create_project = ttk.Entry(master=self._frame)
        create_project_submit = ttk.Button(master=self._frame, text="Add project", command=self._handle_add_project)
        self._create_project.grid(row=2, column=0)
        create_project_submit.grid(row=2, column=1)
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._project_list_frame = ttk.Frame(master=self._frame)
        self._initialize_project_list()
        self._initialize_footer()
        self._project_list_frame.grid(
            row=0,
            column=0,
        )
        

        

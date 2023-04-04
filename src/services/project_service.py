class ProjectService:
    from repositories.project_repository import (
        project_repository as default_project_repository
    )
    
    def __init__(
        self,
        project_repository=default_project_repository
    ):
        self._project_repository = project_repository
    
    def get_all_projects(self):
        return list(self._project_repository.find_all())

project_service = ProjectService()
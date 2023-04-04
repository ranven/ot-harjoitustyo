from db_connection import get_db_connection
from entities.project import Project 

class ProjectRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM projects;")
        rows = cursor.fetchall()
        return [Project(row["title"], row["created_at"]) for row in rows]
 
connection = get_db_connection()    
project_repository = ProjectRepository(connection)
projects = project_repository.find_all()

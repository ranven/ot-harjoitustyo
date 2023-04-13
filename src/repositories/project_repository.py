from db_connection import get_db_connection
from entities.project import Project


class ProjectRepository:
    def __init__(self, db_connection):
        self._connection = db_connection

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM projects")
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM projects")
        rows = cursor.fetchall()
        return [Project(row["title"], row["created_at"]) for row in rows]

    def create(self, title):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO projects (title) values (?)", [title])
        self._connection.commit()
        return title


connection = get_db_connection()
project_repository = ProjectRepository(connection)
projects = project_repository.find_all()

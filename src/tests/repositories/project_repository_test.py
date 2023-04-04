import unittest
import time   
import datetime 
from repositories.project_repository import project_repository
from entities.project import Project

class TestProjectRepository(unittest.TestCase):
    def setUp(self):
        project_repository.delete_all()
        self.projects = [Project(title="testing", created_at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), 
                         Project(title="cleaning", created_at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), 
                         Project(title="schoolwork", created_at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))]
    
    def test_create(self):
        project_repository.create(self.projects[0].title)
        all_projects = project_repository.find_all()
        self.assertEqual(len(all_projects), 1)
        self.assertEqual(all_projects[0].title, self.projects[0].title)
        self.assertEqual(all_projects[0].created_at, self.projects[0].created_at)

    def test_find_all(self):
        i = 0 
        for p in self.projects:
            project_repository.create(p.title)
            all_projects = project_repository.find_all()
            self.assertEqual(len(all_projects), i+1)
            self.assertEqual(all_projects[i].title, self.projects[i].title)
            self.assertEqual(all_projects[i].created_at, self.projects[i].created_at)
            i += 1
    
        
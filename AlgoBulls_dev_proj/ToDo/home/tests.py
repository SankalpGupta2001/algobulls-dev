from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
import base64

class TaskAPITest(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='Sankalp', password='hey123456')

        credentials = base64.b64encode(b'Sankalp:hey123456').decode('utf-8')
        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {credentials}')

        logged_in = self.client.login(username='Sankalp', password='hey123456')
        if not logged_in:
            raise ValueError("Failed to log in the test client.")

        self.task1 = Task.objects.create(
            title="Task 1",
            description="Description for Task 1",
            due_date="2023-12-31T23:59:59Z",
            tags="tag1,tag2",
            status="OPEN"
        )
        self.task2 = Task.objects.create(
            title="Task 2",
            description="Description for Task 2",
            due_date="2023-12-31T23:59:59Z",
            tags="tag2,tag3",
            status="WORKING"
        )

    def test_get_Task(self):
        response = self.client.get('/api/get-tasks/')
         
        self.assertEqual(response.status_code, status.HTTP_200_OK)
   

    def test_save_Task(self):
        data = {
            "title": "New Task",
            "description": "Description for New Task",
            "due_date": "2023-12-31T23:59:59Z",
            "tags": "tag4,tag5",
            "status": "OPEN"
        }
        response = self.client.post('/api/save-tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add assertions to verify task creation and data integrity

    def test_get_By_Id_Task(self):
        response = self.client.get(f'/api/getById-tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to validate the response data for a specific task

    def test_update_Task(self):
        data = {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2023-12-31T23:59:59Z",
            "tags": "tag1,tag5",
            "status": "WORKING"
        }
        response = self.client.put(f'/api/{self.task2.id}/update-tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to verify task update and data integrity

    def test_delete_Task(self):
        response = self.client.delete(f'/api/{self.task2.id}/delete-tasks/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Add assertions to verify task deletion








class TaskIntegrationTest(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='Sankalp', password='hey123456')

        # Set up authentication for the client
        credentials = base64.b64encode(b'Sankalp:hey123456').decode('utf-8')
        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {credentials}')

        # Create tasks
        self.task1 = {
            "title": "Task 1",
            "description": "Description for Task 1",
            "due_date": "2023-12-31T23:59:59Z",
            "tags": "tag1,tag2",
            "status": "OPEN"
        }
        self.task2 = {
            "title": "Task 2",
            "description": "Description for Task 2",
            "due_date": "2023-12-31T23:59:59Z",
            "tags": "tag2,tag3",
            "status": "WORKING"
        }

        # Make API requests to create tasks
        self.client.post('/api/save-tasks/', self.task1, format='json')
        self.client.post('/api/save-tasks/', self.task2, format='json')

    def test_get_tasks(self):
        response = self.client.get('/api/get-tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to verify the response data for fetching all tasks

    def test_get_task_by_id(self):
        task_id = 1  # Change this to the actual task ID
        response = self.client.get(f'/api/getById-tasks/{task_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to validate the response data for a specific task by ID

    def test_update_task(self):
        task_id = 2  # Change this to the actual task ID
        updated_data = {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2023-12-31T23:59:59Z",
            "tags": "tag1,tag5",
            "status": "WORKING"
        }
        response = self.client.put(f'/api/{task_id}/update-tasks/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to verify task update and data integrity

    def test_delete_task(self):
        task_id = 2  # Change this to the actual task ID
        response = self.client.delete(f'/api/{task_id}/delete-tasks/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Add assertions to verify task deletion

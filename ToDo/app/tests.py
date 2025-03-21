from django.test import TestCase, Client
from .models import TodoList
from .models import User
from .forms import LoginUser
from .views import details, completed_todos
from django.urls import reverse, resolve
from datetime import date
import datetime

class TodoListModelTest(TestCase):
    def setUp(self):
        self.assigned = User.objects.create(
            username='test',
            email='test@gmail.com',
            password='test12',
        )
        self.todo = TodoList.objects.create(
            title='Task ABC',
            description='This is the description for my task. hello Hello you there ? Task description is here.',
            due_date=date(2025, 12, 28),
            priority='High',
            status='Pending',
            assigned_by=self.assigned,
            assigned_to=self.assigned,
            created_at=datetime.datetime(2025, 3, 21, 14, 33, 24)
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Task ABC')
        self.assertEqual(self.todo.description, 'This is the description for my task. hello Hello you there ? Task description is here.')
        self.assertEqual(self.todo.due_date, date(2025, 12, 28))
     
        self.assertEqual(self.todo.priority, 'High')
     
     
        self.assertEqual(self.todo.status, 'Pending')
        self.assertEqual(self.todo.assigned_by, self.assigned)
        self.assertEqual(self.todo.assigned_to, self.assigned)

class LoginFormTest(TestCase):
    def test_form_valid(self):
        data = {'username':'Tanishqua', 'password':'aabracadabra'}
        form = LoginUser(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        data = {'username':'Tanishqua', 'password':'aabracadfdgfdgdgdffdsfdsfdabra'}
        form = LoginUser(data=data)
        self.assertFalse(form.is_valid()) # Password length > 20

class DetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.assigned = User.objects.create(
            username='test',
            email='test@gmail.com',
            password='test12',
        )
        self.client.force_login(self.assigned)
        self.todo = TodoList.objects.create(
            title='Task ABC',
            description='This is the description for my task. hello Hello you there ? Task description is here.',
            due_date=date(2025, 12, 28),
            priority='High',
            status='Pending',
            assigned_by=self.assigned,
            assigned_to=self.assigned,
            created_at=datetime.datetime(2025, 3, 21, 14, 33, 24)
        )
    
    def test_detail_view(self):
        id = self.todo.id
        url = f"/details/{id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task ABC')
        self.assertContains(response, 'This is the description for my task. hello Hello you there ? Task description is here.')
    
class TestURLs(TestCase):
    def test_completed_url(self):
        url = reverse('completed_todos')
        self.assertEqual(resolve(url).func, )


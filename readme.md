# Django

Now that we have good understanding of Python it is time to have a strong grasp over its framework - Django. Let's get started!

##### Dt. 03 Mar, 2025.

I will be going through [Django Mastery by Geeky Shows](https://www.youtube.com/playlist?list=PLbGui_ZYuhigUfO47FLx4ocfmo1071hlc) playlist to cover the fundamental concepts.

### Introduction to Django 5.x

- Django is a high-level Python web framework that promotes rapid development and clean, pragmatic design.
- Built-in features include ORM, authentication, middleware, admin panel, and security.
- **Django 5.x** introduces enhancements like performance improvements, async capabilities, and refined security features.
- **Pyenv** can be used to manage multiple Python versions required for different Django projects.

#### pyenv vs. venv

| Feature                   | `pyenv`                                                              | `venv`                                                              |
| ------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Purpose**               | Manages multiple Python versions                                     | Creates isolated virtual environments within a Python version       |
| **Scope**                 | Works system-wide, switching Python versions globally or per project | Works within a specific project to isolate dependencies             |
| **How It Works**          | Installs and manages different Python versions                       | Uses the currently installed Python to create a virtual environment |
| **Usage**                 | Switches between Python versions (e.g., 3.12, 3.13)                  | Isolates packages for a project to avoid conflicts                  |
| **Command Example**       | `pyenv install 3.12.3` → `pyenv global 3.12.3`                       | `python -m venv myenv` → `source myenv/bin/activate`                |
| **Dependency Management** | Doesn't handle packages; only changes Python version                 | Manages dependencies using `pip` inside a virtual environment       |

#### **How They Work Together**

- You can **use `pyenv` to install and switch Python versions**.
- Then, **use `venv` within a specific Python version** to create an isolated environment.

Example:

```bash
pyenv install 3.12.3
pyenv global 3.12.3
python -m venv myenv
source myenv/bin/activate
```

### Install and Uninstall Django

#### Install Django

- Install using pip: `pip install django`
- Verify installation: `django-admin --version`
- Install a specific version: `pip install django==5.x`

#### Uninstall Django

- Use `pip uninstall django`
- Remove project dependencies using `pip freeze | grep django` before uninstalling.

### Create Django Project and Apps

#### Django Project vs Application

- **Project** is the entire Django web application setup.
- **Application** is a modular component within a project handling specific functionalities.

#### Start Project vs Start App

- **`django-admin startproject project_name`**: Creates the project with necessary configurations.
- **`python manage.py startapp app_name`**: Creates an application inside the project.
- A project can have multiple applications handling different features.

#### Directory Structure

- `manage.py`: CLI tool to manage the project.
- `project_name/`: Contains project settings and configurations.
  - `settings.py`: Holds configurations for the project.
  - `urls.py`: URL routing definitions.
  - `wsgi.py` & `asgi.py`: Entry points for WSGI/ASGI servers.
- `app_name/`: Individual application with models, views, and templates.

### Django Architecture

- Django follows the **MVT (Model-View-Template)** architecture.
- **Model**: Handles database operations and defines data structure.
- **View**: Contains business logic and processes user requests.
- **Template**: Manages the presentation layer (HTML, CSS, JS).
- **URL Dispatcher**: Maps URLs to views.
- **ORM (Object-Relational Mapper)**: Allows interaction with the database using Python code instead of SQL.
- **Middleware**: Processes requests and responses globally before reaching views.
- **Admin Interface**: Built-in dashboard for managing application data.

### View

#### Function-Based Views (FBVs)

- Defined as Python functions that handle requests.
- Example:
  ```python
  def home(request):
      return HttpResponse("Hello, Django!")
  ```
- Simple and explicit but may require more boilerplate code.

#### Class-Based Views (CBVs)

- Uses Python classes to handle requests more modularly.
- Example:
  ```python
  from django.views import View
  class HomeView(View):
      def get(self, request):
          return HttpResponse("Hello, Django!")
  ```
- Provides built-in mixins for reusable behaviors like authentication and pagination.

### URL Dispatcher

- Django uses `urls.py` to map URLs to views.
- **Basic URL Configuration:**
  ```python
  from django.urls import path
  from . import views
  urlpatterns = [
      path('', views.home, name='home')
  ]
  ```
- Supports including multiple application URLs using `include()`.
- URL parameters can be captured using `<int:id>`, `<str:slug>`.
- **Multiple Applications:**
  - A Django project can contain multiple apps, each with its own views, models, and URLs.
  - Apps are registered in `settings.py` under `INSTALLED_APPS`.
  - URL routing for different apps can be managed via `include()` to keep URLs modular.

Django's modular architecture and built-in tools make web development efficient and scalable.

See you tomorrow! Good day!

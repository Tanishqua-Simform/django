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

##### Dt. 04 Mar, 2025.

Yesterday, I forgot to mention - I had practiced creating function based views. My progress can be tracked through [Hello_Django](/Hello_Django/) directory.

Today we will cover templates in Django. Also, I read this easy to understand article on MVT -> [Django MVT - GeeksForGeeks](https://www.geeksforgeeks.org/django-project-mvt-structure/)

I have covered till video 17 from the [Geeky Shows playlist](https://www.youtube.com/watch?v=jX90ErC5NR4&list=PLbGui_ZYuhigUfO47FLx4ocfmo1071hlc). The summary is as follows -

### Template

- Django templates are used to define the structure and layout of HTML pages dynamically.
- It follows the **MVT (Model-View-Template)** pattern.
- Templates allow rendering dynamic data from views using Django Template Language (DTL).
- Templates are stored in the `templates/` directory within an app or at the project level.
- Template files typically have a `.html` extension.

#### Creating and Using Templates

1. Create a `templates` directory inside your Django app.
2. Inside `templates/`, create an HTML file (e.g., `home.html`).
3. Load and render the template from a view using `render()`.

   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html')
   ```

4. Configure `TEMPLATES` in `settings.py` to ensure Django can find template directories.

#### Render Dynamic Template

- Dynamic templates allow passing data from views to templates.
- Use the `context` parameter in `render()` to send data.
- Example:
  ```python
  def home(request):
      context = {'name': 'Django', 'version': 5.0}
      return render(request, 'home.html', context)
  ```
- Access variables inside the template:
  ```html
  <h1>Welcome to {{ name }} version {{ version }}</h1>
  ```

#### Django Template Language (DTL)

- DTL is a built-in templating engine used to render data dynamically in Django templates.
- Supports variables, filters, tags, and template inheritance.
- **Syntax:**
  - Variables: `{{ variable_name }}`
  - Tags: `{% tag_name %}` (e.g., `{% for item in list %}`)
  - Filters: `{{ variable|filter_name }}`

##### Template Inheritance

- Allows reusing common HTML structures using `{% block %}` and `{% extends %}`.
- `base.html` (Parent Template):
  ```html
  <html>
    <head>
      <title>{% block title %}Default Title{% endblock %}</title>
    </head>
    <body>
      {% block content %}{% endblock %}
    </body>
  </html>
  ```
- `home.html` (Child Template):
  ```html
  {% extends 'base.html' %} {% block title %}Home Page{% endblock %} {% block
  content %}
  <h1>Welcome to Django</h1>
  {% endblock %}
  ```

##### Variables

- Used to pass dynamic content from views to templates.
- Example:
  ```html
  <p>Hello, {{ user.name }}</p>
  ```

##### Filters

- Modify variables before displaying them.
- Applied using the `|` (pipe) symbol.
- Common Filters:
  - `{{ text|lower }}` → Converts text to lowercase.
  - `{{ text|upper }}` → Converts text to uppercase.
  - `{{ list|length }}` → Returns the length of a list.
  - `{{ date|date:"Y-m-d" }}` → Formats a date.

#### Static Files (CSS, JS, Images)

- Django handles static files like CSS, JavaScript, and images using the `static` directory.
- Configure `STATICFILES_DIRS` in `settings.py`:
  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [BASE_DIR / 'static']
  ```
- Create a `static/` folder inside the app and organize files:
  ```
  static/
      css/
          styles.css
      js/
          scripts.js
      images/
          logo.png
  ```
- Load static files in templates:
  ```html
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  <script src="{% static 'js/scripts.js' %}"></script>
  <img src="{% static 'images/logo.png' %}" alt="Logo" />
  ```
- Run `python manage.py collectstatic` to gather all static files in the `STATIC_ROOT` directory for production.

Alongside, I practiced inside our [Hello_Django directory](/Hello_Django/).

- I practied creating dynamic templates inside [Profile/views.py](/Hello_Django/Profile/views.py) and [templates folder.](/Hello_Django/Profile/templates/Profile/)
- Practiced DTL inside [Profile/likes.html](/Hello_Django/Profile/templates/Profile/likes.html)
- Used Django Static files from templates. [Static files](/Hello_Django/Profile/static/Profile/) and [details.html](/Hello_Django/Profile/templates/Profile/details.html)
- Very interesting task - Manipulate js on click of a button and changes static images inside Django template.
  ![Before](/Snapshots/Output_details.html_1.png)
  ![After](/Snapshots/Output_details.html_2.png)
- Even the css properties of both picture are changed using set attributes method of js.

Later, we all trainees had coding round. I have solved both the questions -> [Check it out](/Coding_round.py)

See you tomorrow! Bye!

##### Dt. 05 Mar, 2025.

Today we'll complete rest of templates. So let's get started -

I have completed till 26th video from [Geeky Shows Playlist](https://www.youtube.com/watch?v=ptE5Y2N9i9Q&list=PLbGui_ZYuhigUfO47FLx4ocfmo1071hlc). Its summary is as follows -

#### Template Inheritance

- Template inheritance allows reusing a base template across multiple pages.
- The base template defines a structure, and child templates extend it.
- Uses `{% block %}` and `{% extends %}`.

##### Base Template (`base.html`)

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}Default Title{% endblock %}</title>
  </head>
  <body>
    <header>{% block header %}{% endblock %}</header>
    <main>{% block content %}{% endblock %}</main>
    <footer>{% block footer %}Default Footer{% endblock %}</footer>
  </body>
</html>
```

##### Child Template (`home.html`)

```html
{% extends 'base.html' %} {% block title %}Home Page{% endblock %} {% block
content %}
<h1>Welcome to Django</h1>
{% endblock %}
```

- If multiple `{% block %}` tags have the same name in a template, Django throws a `TemplateSyntaxError`.
- Each block name must be unique within the same template file.

#### Template Inheritance with Static Files

- Static files (CSS, JS, Images) should be included in the base template and inherited by child templates.
- Load static files in the base template:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}" />
<script src="{% static 'js/script.js' %}"></script>
```

- Child templates inherit these static files without re-declaring them.

#### Add Bootstrap in Django

- Django does not include Bootstrap by default, but you can integrate it manually or via a package.
- Install Django Bootstrap 5:

```sh
pip install django-bootstrap5
```

- Add it to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django_bootstrap5',
]
```

- Load Bootstrap in templates:

```html
{% load bootstrap5 %} {% bootstrap_css %} {% bootstrap_javascript %}
```

- Official Docs: [Django Bootstrap 5](https://django-bootstrap5.readthedocs.io/en/latest/quickstart.html)

#### Add Tailwind in Django

- Tailwind can be integrated using the `django-tailwind` package.
- Install Tailwind:

```sh
pip install django-tailwind
```

- Add it to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'tailwind',
    'theme',
]
```

- Create a Tailwind theme:

```sh
python manage.py tailwind init theme
```

- Run the Tailwind build process:

```sh
python manage.py tailwind start
```

- Official Docs: [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)

#### TailwindCSS CLI

- TailwindCSS CLI is used for direct integration without Django-tailwind.
- Install Tailwind CLI:

```sh
npm install -g tailwindcss
```

- Initialize Tailwind configuration:

```sh
tailwindcss init
```

- Run Tailwind in watch mode:

```sh
tailwindcss -i ./input.css -o ./output.css --watch
```

#### Hyperlink Using `url` Tag

- Django templates use `{% url %}` to create dynamic hyperlinks.
- Example:

```html
<a href="{% url 'home' %}">Home</a>
```

- `home` is the name of a view defined in `urls.py`.
- Passing parameters:

```html
<a href="{% url 'profile' user.id %}">Profile</a>
```

#### Template Inside Template (`include` Tag)

- `{% include %}` is used to insert one template inside another.
- Example:

```html
{% include 'navbar.html' %}
```

- Useful for including headers, footers, and sidebars.

#### Dynamic URL

- Dynamic URLs allow passing parameters to views and generating URLs dynamically.
- Define a URL pattern:

```python
path('post/<int:id>/', views.post_detail, name='post_detail')
```

- Create a dynamic link in a template:

```html
<a href="{% url 'post_detail' id=post.id %}">View Post</a>
```

Along with this, I solved 2 SQL queries and few DSA questions!

Also, we had meeting to discuss about SPL(cricket) and team distribution. So technically, i was not able to complete my today's target but no worries we'll finish it tomorrow!

See you tomorrow! Bye!

crispy form
clean method

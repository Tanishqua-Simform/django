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

##### Dt. 06 Mar, 2025.

Today we will see models and admin panel in Django.

I have completed till 31st video from [Geeky Shows Playlist](https://www.youtube.com/watch?v=ptE5Y2N9i9Q&list=PLbGui_ZYuhigUfO47FLx4ocfmo1071hlc). Its summary is as follows -

### ORM (Object-Relational Mapping)

- ORM allows interaction with the database using Python code instead of SQL queries.
- Django provides a high-level ORM that abstracts database interactions.
- Works with different databases like PostgreSQL, MySQL, SQLite, and Oracle.
- Uses Python classes (models) to define database tables and relationships.

#### Models

- A model in Django is a Python class that represents a table in the database.
- Defined in `models.py` inside a Django app.
- Each class variable represents a field in the table.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
```

#### Common Model Fields:

- `CharField(max_length=...)` – Stores short text values.
- `IntegerField()` – Stores integer values.
- `BooleanField()` – Stores True/False values.
- `DateTimeField(auto_now_add=True)` – Stores date and time when an object is created.
- `ForeignKey()` – Defines a many-to-one relationship.
- `ManyToManyField()` – Defines a many-to-many relationship.

#### Migrations

- Migrations apply changes to the database schema based on model updates.
- Django generates migrations automatically when models are created or updated.

#### Commands:

- `python manage.py makemigrations` – Creates migration files for model changes.
- `python manage.py migrate` – Applies migration files to the database.
- `python manage.py showmigrations` – Lists available migrations.
- `python manage.py sqlmigrate <app_name> <migration_number>` – Shows raw SQL of a migration.

#### Creating a Database

- By default, Django uses SQLite, but other databases can be configured.
- Database settings are defined in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- After defining models, run:

```sh
python manage.py makemigrations
python manage.py migrate
```

#### Retrieving Data

- Django ORM provides methods to fetch data from the database.

1. Fetch All Records:

```python
authors = Author.objects.all()
```

2. Filtering Data:

```python
adults = Author.objects.filter(age__gte=18)
```

3. Getting a Single Record:

```python
author = Author.objects.get(id=1)
```

4. Ordering Data:

```python
sorted_authors = Author.objects.order_by('-age')
```

5. Limiting Query Results:

```python
first_five = Author.objects.all()[:5]
```

6. Counting Records:

```python
count = Author.objects.count()
```

7. Checking Existence:

```python
exists = Author.objects.filter(name='John Doe').exists()
```

8. Related Objects:

- If an `Author` has a ForeignKey to `Book`, access related books using:

```python
author = Author.objects.get(id=1)
books = author.book_set.all()
```

### Admin Panel

- Django provides a built-in admin interface for managing database records.
- Access the admin panel by running the server and visiting `/admin/`.
- Requires superuser creation:

```sh
python manage.py createsuperuser
```

- Enter a username, email, and password when prompted.
- Start the server and log in with the created credentials.

#### Register Model in Admin

- To make a model accessible in the admin panel, register it in `admin.py`.

```python
from django.contrib import admin
from .models import Author

admin.site.register(Author)
```

#### Display Database Data in Admin

- The admin panel allows viewing, adding, editing, and deleting records.
- Customize the admin interface by using `ModelAdmin`.

```python
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
    search_fields = ('name', 'email')
    list_filter = ('age',)

admin.site.register(Author, AuthorAdmin)
```

- `list_display`: Specifies columns to show in the list view.
- `search_fields`: Enables search functionality.
- `list_filter`: Adds filtering options in the admin panel.

Later we had an extensive 4-hr long session on Django by our senior, in that we covered MVT architecture. Extend and Include in templates. Jinja template. And basic to-do list project for data retrieval and creation from admin panel.

I have also started implementing [ToDo](/ToDo/) project myself. It is using sqlite3 as db. I have also implemented create and read operations. As well as filtering pending tasks.

- Have a look
  ![Todo - Admin](/Snapshots/Todo_admin_create.png)

See you tomorrow!

##### Dt. 07 Mar, 2025.

Hello There!
Let's get into Form validation and handling today. Later we'll continue our todo project.

I have watched till 34th video.

### Django Forms

- Django provides a powerful `forms` module to handle form creation, validation, and processing.
- Forms can be created manually or using ModelForms.
- Django forms provide security against CSRF attacks.

#### Creating a Form

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

- `CharField()`: Creates a text input field.
- `EmailField()`: Ensures valid email format.
- `widget=forms.Textarea`: Renders a multi-line input.

#### Handling Form Submission in Views

```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Process data (e.g., save to DB, send email, etc.)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

#### Rendering the Form in a Template

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

### Django Form API

- Provides methods to validate and process form data.

#### Important Methods

- `is_valid()`: Checks if form data is valid.
- `cleaned_data`: Retrieves validated data from form fields.
- `save()`: Used in ModelForms to save data.

### Custom Validation

```python
class CustomForm(forms.Form):
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Must be at least 18 years old.")
        return age
```

### ModelForm

- Automatically generates form fields from a Django model.
- Reduces redundancy by linking the form directly to a model.

```python
from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'age']
```

#### Using ModelForm in a View

```python
def person_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    return render(request, 'person.html', {'form': form})
```

#### Rendering ModelForm in a Template

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

#### Rendering Form Fields Manually

- Instead of using `{{ form.as_p }}`, fields can be rendered individually for better customization.

```html
<form method="post">
  {% csrf_token %}
  <label for="id_name">Name:</label>
  {{ form.name }}
  <label for="id_email">Email:</label>
  {{ form.email }}
  <label for="id_message">Message:</label>
  {{ form.message }}
  <button type="submit">Submit</button>
</form>
```

#### Rendering Form Fields Using a Loop

- Useful when dealing with many form fields dynamically.

```html
<form method="post">
  {% csrf_token %} {% for field in form %}
  <div>
    <label>{{ field.label_tag }}</label>
    {{ field }} {% if field.errors %}
    <small style="color: red;">{{ field.errors }}</small>
    {% endif %}
  </div>
  {% endfor %}
  <button type="submit">Submit</button>
</form>
```

#### Benefits of Loop Rendering

- Dynamically generates form fields.
- Provides a structured way to handle errors.
- Enhances flexibility for UI styling.

#### Jinja Vs. DTL

| Feature                | Jinja2                                        | Django Template Language (DTL)                  |
| ---------------------- | --------------------------------------------- | ----------------------------------------------- |
| **Syntax**             | Python-like, flexible                         | More restrictive, Django-specific               |
| **Performance**        | Faster, optimized for rendering               | Slower, but sufficient for most cases           |
| **Filters & Tags**     | Rich set, supports macros                     | Limited compared to Jinja                       |
| **Whitespace Control** | Allows fine-grained control                   | More rigid and less flexible                    |
| **Extensibility**      | Easily supports custom filters and extensions | Limited customization                           |
| **Security**           | Requires manual escaping for security         | Auto-escapes to prevent XSS                     |
| **Use Case**           | Preferred for flexibility in complex projects | Best for built-in Django templates and security |

Later I resumed working on my To-Do app. I have implemented Create feature using Forms. As well as, integrated bootstrap for attractive UI -> [Styled Home Page](/Snapshots/Todo_Home_Styled.png)

That's it for today! See you on Monday!

##### Dt. 10 Mar, 2025.

Today we will cover all the topics we have learnt so far in more depth to make them stronger.

I have covered -

- MVC vs. MVT architecture.
- Url router is the Controller in MVT.
- ORM is to make database queries from python. It protects from SQL injections and CSRF issues.
- ORM Methods / QuerySet API - create(), save(), update(), delete(), filter(), get()
- Change databases using - dumpdata and loaddata
  - Dumps data of older db into json file and then loads it from json file to new db
- Integrate NoSql in Django using Adapter - djongo. Also, we can use DRF for mongodb
- Data migrations, Conflict in Migration - makemigration --merge
- Fake migration - migrate --fake
- Meta class - Inner class that holds meta data. db_table, verbose_name, permissions etc actions can be performed in it.
- Group by in Django using values() followed by annotate()

For deeper understanding it is better that I provide you the link to my chat with GPT - [Link](https://chatgpt.com/share/67ceee24-1288-8008-8f93-bfe305c00ecb)

Other than this, I helped my co-trainee with her git assignment, as she joined late and had a few conceptual doubts in the basics.
I also helped another trainee with issues in creating form with POST methods and integrating bootstrap in it.

That's it for today. See you tomorrow!

##### Dt. 11 Mar, 2025.

Today we will see Views and Forms in detail.

- **FBV** – Function-Based Views; define views using functions to handle HTTP requests.
- **Redirect and reverse** – `redirect()` sends users to a different URL; `reverse()` generates URLs dynamically using names.
- **HttpResponse and JsonResponse** – `HttpResponse` returns plain HTML; `JsonResponse` returns JSON data.
- **CBV** – Class-Based Views; define views using Python classes for better reusability and organization.
- **Prebuilt CBVs – ListView and DetailView** – `ListView` shows a list of objects; `DetailView` shows details of a single object.
- **Decorators in Views** – `@login_required`, `@csrf_exempt`, etc., modify the behavior of views.
- **CSRF Token and CSRF Exempt** – CSRF token prevents cross-site request forgery; `@csrf_exempt` disables CSRF protection for a view.

- **Forms** – Used to collect and validate user input.
- **Form API** – Provides built-in methods for rendering and validating forms.
- **Custom Validation – use validator attribute** – Use `validators` to define custom validation rules in fields.
- **ModelForm** – A form tied to a database model for quick data handling.
- **Custom Validation – make function with `clean_` prefix** – Define a `clean_<fieldname>()` method to add custom validation logic.
- **Formsets – handle multiple forms** – Manage multiple forms simultaneously using `formsets`.
- **Runserver** – `python manage.py runserver` starts the development server.

For deeper understanding refer this chat -> [Views and Forms](https://chatgpt.com/share/67d048c2-e16c-8008-9cbd-8ead8b42a103)

Along with this, I practiced 10 different scenarios in Views and 6 scenarios in Forms. I will practice a few more tomorrow!

You can checkout the tasks done here -> [Views](/Practice_Tasks/Prac_View/) and [Forms](/Practice_Tasks/Prac_Form/)

See you tomorrow! Bye!

##### Dt. 12 Mar, 2025.

Today we will study Crispy forms, and Authentication in Django.

Before that, I will finish few tasks in [Forms](/Practice_Tasks/Prac_Form/)

- **Crispy Forms**
  - Django Crispy Forms is a third-party package used to render Django forms elegantly with minimal boilerplate code.
  - It supports Bootstrap and other front-end frameworks for styling forms.
  - Provides helper classes and templates to customize form layouts easily.
  - Improves the consistency and appearance of forms across the application.

✅ **When to Use Crispy Forms**

- ✔️ When you want cleaner form rendering.
- ✔️ When you need Bootstrap or Tailwind integration.
- ✔️ When you want to customize form structure without manually adjusting HTML.

- **Authentication**
  - Django provides a built-in authentication framework for handling user login, logout, and registration.
  - Supports user sessions, password hashing, and secure cookies.
  - Provides authentication decorators like `@login_required` for restricting access to views.
  - Includes user model customization for handling user profiles and permissions.
  - Offers authentication backends for using external authentication sources (e.g., OAuth).

Later, I practiced both the concepts. [Crispy Forms](/Practice_Tasks/Prac_Crispy/) and [Authentication](/Practice_Tasks/Prac_Auth/)

I have to integrate password change and permissions in authentication. I will do that tomorrow.

See you! Bye!

##### Dt. 13 Mar, 2025.

Happy Holi!

Today we will complete authentication tasks and permissions.

I have completed few tasks in [Prac_Auth](<(/Practice_Tasks/Prac_Auth/)>)

The resources for authentication can be found from this chat -> [Chatgpt link](https://chatgpt.com/share/67ceee24-1288-8008-8f93-bfe305c00ecb)

Although I haven't achieved much today, it was great bonding with other trainees. So yes, I would consider today's day more towards team bonding!

So that's it fpr today! See you on Monday! After the long weekend!

##### Dt. 17 Mar, 2025.

Today we will see permissions, middleware, static and media files.

#### Permissions

- Django permissions control access to views, models, and actions based on user roles.
- Default permissions (`add`, `change`, `delete`, `view`) are automatically created for each model.
- Permissions are assigned at the user and group level.

**Custom Permissions**

- Custom permissions can be defined in the `Meta` class of a model using the `permissions` attribute.
- Example:
  ```python
  class MyModel(models.Model):
      class Meta:
          permissions = [("can_publish", "Can publish articles")]
  ```

**Group Permissions**

- Groups allow assigning permissions collectively to multiple users.
- Users inherit all permissions assigned to the group.
- Example: Create an `editor` group and assign permissions to it.

**@permission_required Decorator**

- Restricts access to a view based on user permissions.
- Example:
  ```python
  @permission_required('app.can_publish')
  def my_view(request):
      pass
  ```

**has_perm() Method**

- Checks if a user has a specific permission.
- Example:
  ```python
  if request.user.has_perm('app.can_publish'):
      pass
  ```

**Restricting Views**

- `@login_required` – Requires user authentication.
- `@permission_required` – Requires user to have specific permissions.
- `PermissionRequiredMixin` – Restricts class-based views.

**PermissionRequiredMixin**

- Used in class-based views to restrict access based on permissions.
- Example:

  ```python
  from django.contrib.auth.mixins import PermissionRequiredMixin

  class MyView(PermissionRequiredMixin, View):
      permission_required = 'app.can_publish'
  ```

#### Middleware

- Middleware is a lightweight, low-level plugin used to process requests and responses globally before passing them to views.
- Defined as a list in `MIDDLEWARE` setting in `settings.py`.

**\_\_init\_\_()**

- Called when the middleware is initialized.
- Used to perform setup tasks.

**\_\_call\_\_()**

- Called for each request.
- Must return a response object.

**get_response()**

- Called when processing a request or returning a response.
- Returns a response object.

**process_view()**

- Called before the view function is executed.
- Can modify the request or return a response directly.

**process_exception()**

- Called if the view raises an exception.
- Can handle the exception or return an error response.

**process_template_response()**

- Called after the view returns a `TemplateResponse`.
- Can modify the response before rendering.

#### Static Files and Media Files

- Static files include CSS, JavaScript, and images used in the frontend.
- Media files include user-uploaded content like images and documents.

**Static Files**

- Defined in `STATIC_URL` and `STATICFILES_DIRS` settings.
- Example:
  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [BASE_DIR / 'static']
  ```
- Use `{% static 'path/to/file' %}` in templates.

**Media Files**

- Defined in `MEDIA_URL` and `MEDIA_ROOT` settings.
- Example:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- Use `models.FileField` and `models.ImageField` for handling uploads.
- Files are served during development using `django.views.static.serve`.

For detailed explanation of any topic refer this chat -> [ChatGPT](https://chatgpt.com/share/67ceee24-1288-8008-8f93-bfe305c00ecb)

Later, I implemented CRUD operations and authentication in my [TODO](/ToDo/) app.

![Todo Crud](/Snapshots/Todo_CRUD.png)

That's it for today! See you tomorrow!

##### Dt. 18 Mar, 2025.

Today we will learn to customize Admin Panel and Signals.

#### Admin Panel Customization

- Django Admin is a built-in interface for managing database models and data.
- It is enabled by adding `'django.contrib.admin'` in `INSTALLED_APPS`.
- The admin interface can be accessed at `/admin` after running `python manage.py createsuperuser`.

**list_display**

- Controls which fields are shown in the admin list view.
- Example:

  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      list_display = ('title', 'author', 'published_date')
  ```

**search**

- Allows searching within admin list views.
- Example:
  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      search_fields = ('title', 'content')
  ```

**filter**

- Adds filter options in the admin interface.
- Example:
  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      list_filter = ('status', 'author')
  ```

**read_only**

- Makes fields read-only in the admin interface.
- Example:
  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      readonly_fields = ('slug',)
  ```

**prepopulated_fields**

- Automatically generates values for fields based on other fields.
- Example:
  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      prepopulated_fields = {'slug': ('title',)}
  ```

**actions**

- Allows adding custom actions to the admin interface.
- Example:

  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      actions = ['publish']

      def publish(self, request, queryset):
          queryset.update(status='published')
  ```

**grouping fields**

- Groups related fields together in the admin interface.
- Example:
  ```python
  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      fieldsets = (
          ('Content', {'fields': ('title', 'body')}),
          ('Metadata', {'fields': ('author', 'status', 'slug')}),
      )
  ```

**inlines**

- Displays related models within the same admin interface.
- Example:

  ```python
  class CommentInline(admin.TabularInline):
      model = Comment
      extra = 1

  @admin.register(Post)
  class PostAdmin(admin.ModelAdmin):
      inlines = [CommentInline]
  ```

**admin title**

- Changes the title of the admin panel.
- Example:
  ```python
  admin.site.site_header = "My Blog Admin"
  admin.site.site_title = "Blog Admin Panel"
  admin.site.index_title = "Welcome to Blog Admin"
  ```

**slug**

- A slug is a URL-friendly identifier, often generated from a model field like `title`.
- Example:

  ```python
  from django.utils.text import slugify

  class Post(models.Model):
      title = models.CharField(max_length=200)
      slug = models.SlugField(unique=True)

      def save(self, *args, **kwargs):
          if not self.slug:
              self.slug = slugify(self.title)
          super().save(*args, **kwargs)
  ```

#### Signals

- Signals allow decoupled components to get notified when certain actions occur.
- They enable communication between different parts of a Django application.
- Useful for performing actions automatically when certain events happen.

**Creating a Signal**

- A signal is created using `django.dispatch.signal`.
- Example:

  ```python
  from django.db.models.signals import post_save
  from django.dispatch import receiver
  from .models import Post

  @receiver(post_save, sender=Post)
  def create_slug(sender, instance, created, **kwargs):
      if created:
          instance.slug = slugify(instance.title)
          instance.save()
  ```

**Connecting Signals**

- Signals are connected using `@receiver` decorator or `connect` method.
- Example using `connect` method:

  ```python
  from django.db.models.signals import post_save
  from .models import Post

  def create_slug(sender, instance, created, **kwargs):
      if created:
          instance.slug = slugify(instance.title)
          instance.save()

  post_save.connect(create_slug, sender=Post)
  ```

**Types of Signals**

- **pre_save** – Triggered before a model’s `save()` method is called.
- **post_save** – Triggered after a model’s `save()` method is called.
- **pre_delete** – Triggered before a model’s `delete()` method is called.
- **post_delete** – Triggered after a model’s `delete()` method is called.
- **m2m_changed** – Triggered when a `ManyToManyField` is modified.
- **request_started** – Triggered when a request starts processing.
- **request_finished** – Triggered when a request finishes processing.
- **got_request_exception** – Triggered when an exception occurs during request processing.

**Disconnecting Signals**

- A signal can be disconnected using the `disconnect()` method.
- Example:
  ```python
  post_save.disconnect(create_slug, sender=Post)
  ```

**Use Cases**

- Creating slugs from titles automatically.
- Sending email notifications when a user registers.
- Logging user activities.
- Caching data after an object is saved.

For in depth knowledge, refer this chat -> [ChatGpt link](https://chatgpt.com/share/67ceee24-1288-8008-8f93-bfe305c00ecb)

Later, I integrated Role-based authentication using groups and permissions in my Todo app as suggested by my mentor, with 2 roles.

- Mentor - Can create, update and delete tasks
- Mentee - Can only View tasks.

I have also implemented profile photo updation functionality using media files. I have to add resume updation feature, so as to manipulate pdf files.

I have also customized admin panel with list of models, search and filter functionality. I have changed the site_title, index_title and site_header of admin panel as well.

That's it for today! See you tomorrow!

##### Dt. 19 Mar, 2025.

Today we will implement middleware and signals in Todo app and read about jinja template and custom template tags.

#### Jinja Template

- Jinja is a fast, expressive, and extensible templating engine used in Django.
- It allows embedding Python-like expressions within HTML.
- Syntax is similar to DTL (Django Template Language) but more powerful and flexible.
- Used for rendering dynamic content in templates.
- Example:
  ```html
  {% for item in items %} {{ item.name }} {% endfor %}
  ```

**Custom Template Tags**

- Custom template tags allow adding custom logic in templates.
- Defined using `{% register %}` in a `templatetags` directory.
- Example:

  1.  Create a `templatetags` directory inside the app.
  2.  Create a `custom_tags.py` file:

      ```python
      from django import template
      register = template.Library()

      @register.simple_tag
      def add(x, y):
          return x + y
      ```

  3.  Use in the template:
      ```html
      {% load custom_tags %} {% add 5 10 %}
      ```

**Built-in Template Tags**

- Predefined tags provided by Django for common tasks.
- **Control flow tags**:

  - `{% if %}...{% endif %}` – Conditional statements.
  - `{% for %}...{% endfor %}` – Loop through iterable objects.
  - `{% block %}...{% endblock %}` – Define and override template blocks.
  - `{% include %}` – Include another template.
  - `{% extends %}` – Extend a base template.
  - `{% with %}` – Create a temporary context variable.
  - `{% csrf_token %}` – Protect against CSRF attacks.

- **Template Inheritance**:

  - `{% block %}` and `{% extends %}` allow creating reusable templates.
  - Example:

    ```html
    {% extends 'base.html' %} {% block content %}
    <h1>Welcome</h1>
    {% endblock %}
    ```

**Filters**

- Filters modify the value of a variable before rendering.
- Applied using the `|` (pipe) operator.
- Example:

  ```html
  {{ name|lower }} {{ price|floatformat:2 }}
  ```

- **Common Built-in Filters**:
  - `lower` – Converts string to lowercase.
  - `upper` – Converts string to uppercase.
  - `length` – Returns the length of an object.
  - `default` – Sets a default value if the value is None.
  - `floatformat` – Formats a float to a specific number of decimal places.
  - `date` – Formats a date object.
  - `escape` – Escapes HTML special characters.
  - `truncatechars` – Truncates a string to a specific length.
  - `safe` – Marks a string as safe to render HTML.

**Use Cases**

- Custom template tags are used when logic is too complex for filters.
- Filters are used for formatting and simple transformations.
- Jinja templates are used to separate logic from presentation, making code cleaner.

Later, I implemented custom middleware in the Todo App. It records the last login time of users and the number of times they have logged in. It also stores the total requests that the server has served in its lifetime.

I have also created custom signals for create, update and delete task views. Whenever the signal is triggered it sends an email to the assignee about the change.

You can track the progress here -> [Todo App](/ToDo/app/middleware/user_visits.py)

That's it for today! See you tomorrow!

##### Dt. 20 Mar, 2025.

Today we will see test cases in django as well as Jinja template and custom template tags in detail.

#### Test Cases

- Test cases are used to verify the correctness of code in Django.
- Django provides a `unittest`-based testing framework.
- Tests ensure that the application behaves as expected after changes.

**Types of Test Cases**

- **Unit Tests** – Test individual units of code (e.g., functions, models).
- **Integration Tests** – Test how different components work together.
- **Functional Tests** – Test user-facing behavior.

**Creating a Test Case**

- Create a `tests.py` file inside the app.
- Example:

  ```python
  from django.test import TestCase
  from .models import Item

  class ItemModelTest(TestCase):
      def test_item_creation(self):
          item = Item.objects.create(name="Test Item")
          self.assertEqual(item.name, "Test Item")
  ```

**Running Tests**

- Run all tests:
  ```bash
  python manage.py test
  ```
- Run tests in a specific app:
  ```bash
  python manage.py test myapp
  ```
- Run a specific test file:
  ```bash
  python manage.py test myapp.tests
  ```

**Assertions**

- `assertEqual(a, b)` – Checks if `a == b`.
- `assertNotEqual(a, b)` – Checks if `a != b`.
- `assertTrue(x)` – Checks if `x` is `True`.
- `assertFalse(x)` – Checks if `x` is `False`.
- `assertIsNone(x)` – Checks if `x` is `None`.
- `assertIsNotNone(x)` – Checks if `x` is not `None`.
- `assertRaises(Exception)` – Checks if an exception is raised.

**TestCase Methods**

- `setUp()` – Called before each test method.
- `tearDown()` – Called after each test method.
- `setUpTestData()` – Sets up data at the class level (called once).

**Client Testing**

- Django provides a `Client` class for simulating HTTP requests.
- Example:

  ```python
  from django.test import Client

  def test_homepage(self):
      client = Client()
      response = client.get('/')
      self.assertEqual(response.status_code, 200)
  ```

**Testing Views**

- Example:
  ```python
  def test_view(self):
      response = self.client.get('/my-view/')
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'my_template.html')
  ```

**Testing Models**

- Example:
  ```python
  def test_model(self):
      item = Item.objects.create(name="Test Item")
      self.assertEqual(str(item), "Test Item")
  ```

**Testing Forms**

- Example:
  ```python
  def test_form_valid(self):
      form = MyForm(data={'name': 'Test'})
      self.assertTrue(form.is_valid())
  ```

**Testing Signals**

- Example:

  ```python
  from django.db.models.signals import post_save

  def test_signal(self):
      with self.assertSignal(post_save):
          Item.objects.create(name="Test Item")
  ```

**TestCase Best Practices**

- Write tests for both success and failure cases.
- Keep tests isolated from external services.
- Use `setUpTestData()` for reusable test data.
- Keep test names descriptive.
- Avoid hardcoding data; use dynamic values where possible.

To get in depth understanding of topics covered till now refer this chat -> [ChatGPT](https://chatgpt.com/share/67ceee24-1288-8008-8f93-bfe305c00ecb)

Later I implemented DRY principle in my Todo App and cleaned the templates by reusing the code (block and extends tag were helpful in this!)

During that I encountered a problem in which my prettier extension was incorrectly formatting my templates, so I installed beautify extension instead. For configuration refer this blog: [Beautify for templates](https://gotofritz.net/blog/fixing-autoformatting-django-templates-in-visual-studio-code/)

I discovered about XSS attacks and how django prevents it by using escaping feature: [GFG article](https://www.geeksforgeeks.org/cross-site-scripting-xss-protection-in-django/)

I have also implemented search bar functionality in My todos page from the backend, although it requires to reload the page which is not efficient. Instead we should use JS Dom manipulation and AJAX calls for efficiency.

Along with this, I have removed Navbar from Login and Register page.

So that's it for today! See you tomorrow!

P.S. I have a practice match for SPL later today! Will let you know how it goes tomorrow. Toodles!

##### Dt. 21 Mar, 2025.

Today we will implement Test cases and read about channels.

#### Channels

- Django Channels extends Django to handle real-time asynchronous communications like WebSockets, chat applications, and background tasks.
- It integrates with Django's request/response cycle but allows asynchronous features.
- Uses **Daphne** as an ASGI server to process requests asynchronously.
- Supports WebSockets, long polling, and other async protocols.

**Key Concepts**

- **Consumers**: Handle WebSocket connections like Django views handle HTTP requests.
- **Routing**: Similar to Django URL routing but for WebSockets.
- **Layers**: Uses Redis for message passing between different parts of the application.
- **Middleware Stacks**: Modify incoming WebSocket requests like Django’s middleware.

**Use Cases**

- Real-time chat applications
- Live notifications
- Background task processing
- Multiplayer gaming

#### Custom Response, Exceptions, and Mixins

**Custom Response**

- Django provides `HttpResponse` and `JsonResponse` to return custom responses.
- You can customize status codes, headers, and response formats.

**Examples**

```python
from django.http import JsonResponse, HttpResponse

def custom_json_response(request):
    data = {"message": "Success", "status": 200}
    return JsonResponse(data, status=200)

def custom_text_response(request):
    return HttpResponse("Custom Text Response", content_type="text/plain", status=201)
```

**Custom Exceptions**

- Django provides built-in exceptions like `Http404` and `PermissionDenied`, but custom exceptions help in handling specific errors.

**Creating Custom Exceptions**

```python
class CustomAPIException(Exception):
    def __init__(self, message="Custom error occurred"):
        self.message = message
        super().__init__(self.message)
```

**Raising Custom Exceptions in Views**

```python
from django.http import JsonResponse

def custom_exception_view(request):
    raise CustomAPIException("Invalid operation")
```

**Handling Custom Exceptions**

```python
from django.core.exceptions import PermissionDenied

def custom_error_handler(request):
    try:
        # Some operation
        pass
    except PermissionDenied:
        return JsonResponse({"error": "Permission Denied"}, status=403)
    except CustomAPIException as e:
        return JsonResponse({"error": str(e)}, status=400)
```

**Mixins**

- Mixins are reusable classes that provide additional functionality to Django views.
- Used in **Class-Based Views (CBVs)** to enhance functionality without duplication.

**Common Django Mixins**

- `LoginRequiredMixin` – Restricts access to authenticated users.
- `PermissionRequiredMixin` – Restricts access based on user permissions.
- `UserPassesTestMixin` – Restricts access based on custom conditions.

**Example Usage**

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Item

class SecureItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'items.html'
    login_url = '/login/'  # Redirect to login if not authenticated
```

**Custom Mixin**

```python
class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return JsonResponse({"error": "Admin access required"}, status=403)
        return super().dispatch(request, *args, **kwargs)
```

**When to Use Mixins?**

✔ When you need reusable functionality across multiple views.  
✔ When following **DRY (Don't Repeat Yourself)** principles.  
✔ When you need authentication, permission checks, or custom behavior in CBVs.

Along with this, I have implemented test cases for models, views and forms in [tests.py](/ToDo/app/tests.py)

I have used Client() to simulate browser request in test cases.

I found this interesting issue on Multiple Inheritance of models in Django using Abstract Models [StackOverFlow](https://stackoverflow.com/questions/6428075/is-it-ok-to-use-multiple-inheritance-with-django-abstract-models)

So that's it for today! See you on Monday.

P.S. - Cricket Update - So it was quite fun yesterday @ the practice match, although we lost I am happy that our team gave its best. Toodles!

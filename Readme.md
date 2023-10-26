# Blogr

Welcome to Blogr, a dynamic and user-friendly Django-based blog application designed to empower your creativity and content sharing journey. Whether you're a seasoned writer, aspiring blogger, or simply passionate about storytelling, Blogr offers the perfect platform to craft and share your narratives with the world.

🌟 Key Features:

    #### User-Friendly Interface: Seamlessly navigate through a clean and intuitive user interface.
    #### Rich Text Editing: Create stunning, multimedia-rich blog posts with our powerful editor.
    #### User Authentication: Secure user registration and login system.
    #### Comments and Feedback: Engage with your audience through comments and feedback.
    #### Image Uploads: Easily upload and embed images to enhance your content.
    #### Author Profiles: Showcase your author bio and links to your social profiles.
    #### Responsive Design: Enjoy a consistent experience on all devices.
    
## Getting Started

Follow the steps below to set up and run the Blogr project.

### Prerequisites

Make sure you have Python and pip installed on your system.

### Setup Virtual Environment

Create a virtual environment for your project:

```bash
python3 -m venv blenv
```

Activate the virtual environment:

- On Linux:

```bash
source blenv/bin/activate
```

### Install Django

Install Django using pip:

```bash
pip install django
```

### Create Django Project

Create a new Django project named 'blog':

```bash
django-admin startproject blog
```

Change to the project directory:

```bash
cd blog
```

Create a new app named 'website':

```bash
python manage.py startapp website
```

### Set Up Environment Variables

Install the `python-dotenv` package to use environment variables in your project:

```bash
pip install python-dotenv
```

Create a `.env` file to store sensitive credentials. For example, you can include your `SECRET_KEY`:

```
SECRET_KEY=your_secret_key_here
```

Modify the `settings.py` file to load credentials from the `.env` file:

```python
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
```

### Configure Installed Apps

In your `settings.py` file, add your 'website' app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',  # Add your 'website' app here
]
```

### Apply Migrations

Apply database migrations to create the necessary tables:

```bash
python manage.py migrate
```

### Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

You can access the project at [http://localhost:8000](http://localhost:8000).

### Create a Superuser

Create an admin user for accessing the admin control panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, password, and other details.

## Usage

You can start building your blog by creating templates, views, and models in the 'website' app. Customize your blog according to your requirements.

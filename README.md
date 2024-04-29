# Django Project Configuration Guide

This guide provides instructions for configuring a Django project with a custom user model, configuring templates, and managing static files.

## Custom User Model (AbstractUser)

### 1. Create a Custom User Model:

- Create a new Django app (if not already created) to store the custom user model.
- Define a custom user model by subclassing `AbstractUser` in your app's `models.py` file.
- Customize the user model fields as per your requirements (e.g., add additional fields).

Example:
```python
# myapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    pass

# settings.py

AUTH_USER_MODEL = 'myapp.CustomUser'

### 2. Create Templates Directory:

- Create a new Django app (if not already created) to store the custom user model.
- Define a custom user model by subclassing `AbstractUser` in your app's `models.py` file.
- Customize the user model fields as per your requirements (e.g., add additional fields).

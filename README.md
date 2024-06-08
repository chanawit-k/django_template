# Django Project Configuration Guide

This guide provides instructions for configuring a Django project with a custom user model, configuring templates, managing static files, configuring mysql DB.

## 1. Custom User Model (AbstractUser):


- Create a new Django app (if not already created) to store the custom user model.
- Define a custom user model by subclassing `AbstractUser` in your app's `models.py` file.
- Customize the user model fields as per your requirements (e.g., add additional fields).

### accounts/model.py
```python

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    pass
```

### settings.py
```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```


### admin.py
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
```
### urls.py
``` python
from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.SampleView.as_view(), name='sample_view'),
]
```
## 2. Configuration of Templates:

- Create a new directory named `templates`

### settings.py
```python

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        ...
        'DIRS': [TEMPLATES_DIR],
        ...
    },
]

```

## 3. Configuring Static Files:

- Create a new directory named `static`.

### settings.py
```python
import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

```

## 4. Configuring MySQL DB:

### settings.py
```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample_db_django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }

}
```

## 5. configuration media url:
## urls.py
``` python
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    ...
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
## settings.py
```python

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

## 6. add gitignore:
``` python
*.pyc
.idea
/.venv
/.vscode

```






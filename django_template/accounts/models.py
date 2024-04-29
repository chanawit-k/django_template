from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, help_text="ชื่อ")
    last_name = models.CharField(max_length=255, blank=True, help_text="นามสกุล")
    phone_number = models.CharField(max_length=255, blank=True, db_index=True, help_text="เบอร์โทรศัพท์")
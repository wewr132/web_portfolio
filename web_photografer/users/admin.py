from django.contrib import admin
from .models import User

# Простая регистрация модели в админке
admin.site.register(User)

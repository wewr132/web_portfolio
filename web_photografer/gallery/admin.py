from django.contrib import admin
from .models import Category, Photo, SiteInfo

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(SiteInfo)
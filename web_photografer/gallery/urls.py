from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/category/<slug:category_slug>/', views.portfolio, name='category_filter'),
]

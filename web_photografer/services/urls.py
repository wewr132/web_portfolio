from django.urls import path

from .views import OrderCreateView, OrderListView, ReviewListView, ReviewCreateView

app_name = 'services'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('my-orders/', OrderListView.as_view(), name='list'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
]

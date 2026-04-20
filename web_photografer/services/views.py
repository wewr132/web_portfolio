from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Order, Review
from .forms import OrderCreateForm, ReviewCreateForm


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderCreateForm
    template_name = 'services/order_form.html'
    success_url = reverse_lazy('services:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'services/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all().order_by('-date')
        return Order.objects.filter(user=self.request.user).order_by('-date')


class ReviewListView(ListView):
    model = Review
    template_name = 'services/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(is_published=True).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewCreateForm()
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = ReviewCreateForm
    template_name = 'services/review_form.html'
    success_url = reverse_lazy('services:review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_published = False
        messages.success(self.request, 'Ваш отзыв отправлен на модерацию.')
        return super().form_valid(form)
